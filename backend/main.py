import os
import httpx

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


# --------------------------------------------------
# HOME
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "AI Backend is running"
    }


# --------------------------------------------------
# GET AVAILABLE OLLAMA MODELS
# --------------------------------------------------

@app.get("/models")
async def get_models():

    api_key = os.getenv("OLLAMA_API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="OLLAMA_API_KEY is not configured"
        )

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    try:

        async with httpx.AsyncClient(timeout=30) as client:

            response = await client.get(
                "https://ollama.com/api/tags",
                headers=headers
            )

        if response.status_code != 200:

            raise HTTPException(
                status_code=response.status_code,
                detail=response.text
            )

        return response.json()

    except HTTPException:
        raise

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


# --------------------------------------------------
# CHAT
# --------------------------------------------------

@app.post("/chat")
async def ask_ai(request: ChatRequest):

    # Check whether we are running in cloud mode
    api_key = os.getenv("OLLAMA_API_KEY")


    # --------------------------------------------------
    # CLOUD MODE
    # --------------------------------------------------

    if api_key:

        model = os.getenv(
            "OLLAMA_MODEL",
            "glm-5.1"
        )

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": request.message
                }
            ],
            "stream": False
        }

        try:

            async with httpx.AsyncClient(timeout=120) as client:

                response = await client.post(
                    "https://ollama.com/api/chat",
                    headers=headers,
                    json=payload
                )


            # Return the real Ollama error
            if response.status_code != 200:

                raise HTTPException(
                    status_code=response.status_code,
                    detail=response.text
                )


            data = response.json()

            return {
                "response": data["message"]["content"],
                "model": model
            }


        except HTTPException:
            raise


        except Exception as error:

            raise HTTPException(
                status_code=500,
                detail=str(error)
            )


    # --------------------------------------------------
    # LOCAL MODE
    # --------------------------------------------------

    else:

        try:

            from ollama import chat

            response = chat(

                model="llama3.2:latest",

                messages=[
                    {
                        "role": "user",
                        "content": request.message
                    }
                ],
            )

            return {
                "response": response.message.content,
                "model": "llama3.2:latest"
            }


        except Exception as error:

            raise HTTPException(
                status_code=500,
                detail=str(error)
            )