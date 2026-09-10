# AI Assistant using FastAPI, Ollama and Vercel

A simple full-stack Generative AI chatbot application built using Python, FastAPI, Ollama, HTML, CSS, JavaScript, Vercel, and GitHub.

The application supports both local Ollama models for development and Ollama Cloud models for deployed environments.

---

## Project Overview

This project demonstrates how to build a complete Generative AI application with a frontend, backend API, and Large Language Model integration.

The user enters a question in the web interface. The frontend sends that question to the FastAPI backend. The backend communicates with Ollama and returns the generated AI response to the frontend.


## Live Application

You can access the deployed AI Assistant here:

[Open AI Assistant](https://chatbotfrontend-omega.vercel.app/)

> The application frontend and backend are hosted on Vercel, and the AI responses are generated using Ollama Cloud.


### Application Flow

```text
User
  ↓
Frontend
HTML + CSS + JavaScript
  ↓
FastAPI Backend
Python
  ↓
Ollama
  ↓
Large Language Model
  ↓
Generated Response
  ↓
Frontend
```

---

## Project Structure

```text
ChatBot_1/
│
├── backend/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .gitignore
│
└── README.md
```

---

## Features

- AI chatbot web interface
- Python FastAPI backend
- REST API integration
- Ollama local model support
- Ollama Cloud model support
- Responsive frontend
- User and AI message bubbles
- Loading animation
- Enter key support for sending messages
- Error handling
- Local development support
- Vercel deployment
- Environment variable based API-key management
- GitHub source-code management

---

## Technology Stack

| Component | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python |
| API Framework | FastAPI |
| LLM Platform | Ollama |
| Local Model | Llama 3.2 |
| Cloud Model | gpt-oss:20b |
| Frontend Hosting | Vercel |
| Backend Hosting | Vercel |
| Source Control | Git & GitHub |

---

# Prerequisites

Before running the project locally, install the following:

- Python
- Ollama
- Git
- VS Code or another code editor

---

## Check Python Installation

Open PowerShell or the VS Code terminal and run:

```bash
python --version
```

Example:

```text
Python 3.12.x
```

---

## Check Ollama Installation

Run:

```bash
ollama --version
```

---

## Check Git Installation

Run:

```bash
git --version
```

Example:

```text
git version 2.x.x.windows.x
```

---

# How to Run the Application Locally

## Step 1 - Clone the GitHub Repository

If the project is already available locally, you can skip this step.

Otherwise run:

```bash
git clone https://github.com/YOUR-USERNAME/chatbot1.git
```

Then go inside the project:

```bash
cd chatbot1
```

---

## Step 2 - Create Python Virtual Environment

From the project root folder run:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

After activation you should see:

```text
(.venv)
```

in your terminal.

---

## Step 3 - Install Python Dependencies

Run:

```bash
python -m pip install -r backend/requirements.txt
```

The main Python packages used in the project are:

```text
fastapi
uvicorn
httpx
ollama
```

---

# Running with Local Ollama

When `OLLAMA_API_KEY` is not configured, the backend uses the locally installed Ollama model.

## Step 4 - Download Llama 3.2

Run:

```bash
ollama pull llama3.2
```

Check installed models:

```bash
ollama list
```

You should see:

```text
llama3.2:latest
```

---

## Step 5 - Test Ollama

Run:

```bash
ollama run llama3.2
```

Ask a question:

```text
What is Generative AI?
```

If the model gives you a response, Ollama is working properly.

To exit:

```text
/bye
```

---

# Running the FastAPI Backend

## Step 6 - Start the Backend

From the root project directory run:

```bash
uvicorn backend.main:app --reload
```

The backend will start at:

```text
http://127.0.0.1:8000
```

You should see output similar to:

```text
Uvicorn running on http://127.0.0.1:8000
```

---

## Step 7 - Test the Backend

Open this URL in your browser:

```text
http://127.0.0.1:8000
```

Expected response:

```json
{
    "message": "AI Backend is running"
}
```

---

## Step 8 - Open FastAPI Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to test the API directly from the browser.

Select:

```text
POST /chat
```

Click:

```text
Try it out
```

Enter:

```json
{
    "message": "What is Generative AI?"
}
```

Click:

```text
Execute
```

You should receive an AI-generated response.

---

# Running the Frontend

Keep the backend terminal running.

Open another PowerShell or VS Code terminal.

Go to the frontend directory:

```bash
cd frontend
```

Start a simple Python HTTP server:

```bash
python -m http.server 5500
```

The frontend will be available at:

```text
http://localhost:5500
```

Open this URL in your browser.

You should now see the AI Assistant interface.

---

## Local Application Architecture

```text
Browser
http://localhost:5500
        ↓
HTML + CSS + JavaScript
        ↓
FastAPI
http://127.0.0.1:8000
        ↓
Local Ollama
        ↓
llama3.2
        ↓
AI Response
```

---

# Local Backend Configuration

The backend automatically uses local Ollama when this environment variable is not present:

```text
OLLAMA_API_KEY
```

The local model used by the project is:

```text
llama3.2:latest
```

The basic local request flow is:

```text
Frontend
   ↓
FastAPI
   ↓
Ollama installed on local computer
   ↓
llama3.2
```

---

# Ollama Cloud Mode

The deployed version of the application uses Ollama Cloud.

The backend checks for the following environment variable:

```text
OLLAMA_API_KEY
```

If the API key exists, the application uses Ollama Cloud instead of local Ollama.

The deployed cloud model currently used is:

```text
gpt-oss:20b
```

The Vercel environment variables are:

```text
OLLAMA_API_KEY
OLLAMA_MODEL
```

Example model configuration:

```text
OLLAMA_MODEL=gpt-oss:20b
```

---

## API Key Security

Never hard-code your Ollama API key inside Python code.

Do not do this:

```python
api_key = "my-secret-api-key"
```

Instead use:

```python
api_key = os.getenv("OLLAMA_API_KEY")
```

The actual API key should be stored securely in Vercel Environment Variables.

---

# Backend API Endpoints

## Home Endpoint

```http
GET /
```

Purpose:

Check whether the backend is running.

Example response:

```json
{
    "message": "AI Backend is running"
}
```

---

## Chat Endpoint

```http
POST /chat
```

Example request:

```json
{
    "message": "Explain machine learning in simple words"
}
```

Example response:

```json
{
    "response": "Machine learning is...",
    "model": "gpt-oss:20b"
}
```

---

## Models Endpoint

```http
GET /models
```

This endpoint returns the Ollama models available through the configured Ollama Cloud account.

---

# Local Mode vs Cloud Mode

## Local Mode

```text
Frontend
    ↓
FastAPI
    ↓
Local Ollama
    ↓
llama3.2
```

## Cloud Mode

```text
Frontend
    ↓
Vercel FastAPI Backend
    ↓
Ollama Cloud
    ↓
gpt-oss:20b
```

The application automatically determines which mode to use based on whether `OLLAMA_API_KEY` exists.

---

# Deployment Architecture

The application is deployed using Vercel.

## Frontend Deployment

```text
HTML
CSS
JavaScript
    ↓
Vercel
```

## Backend Deployment

```text
FastAPI
    ↓
Vercel
    ↓
Ollama Cloud API
```

## Complete Production Architecture

```text
User
  ↓
Vercel Frontend
  ↓
JavaScript HTTPS Request
  ↓
Vercel FastAPI Backend
  ↓
Ollama Cloud API
  ↓
gpt-oss:20b
  ↓
Generated AI Response
  ↓
Frontend
```

---

# Frontend to Backend Communication

The frontend sends the user's message to the deployed backend using JavaScript.

Example:

```javascript
const response = await fetch(
    "https://YOUR-BACKEND.vercel.app/chat",
    {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })
    }
);
```

The frontend should never contain the Ollama API key.

---

# Environment Variables

The following environment variables are configured securely in Vercel:

| Variable | Purpose |
|---|---|
| `OLLAMA_API_KEY` | Authenticates the backend with Ollama Cloud |
| `OLLAMA_MODEL` | Defines which Ollama Cloud model should be used |

Current model:

```text
gpt-oss:20b
```

---

# GitHub

GitHub is used to store and manage the source code for this project.

The application itself is currently hosted on Vercel.

```text
GitHub
    ↓
Source Code Repository

Vercel
    ↓
Frontend + Backend Hosting

Ollama Cloud
    ↓
AI Model
```

---

# Git Commands

## Initialize Git

```bash
git init
```

## Check Status

```bash
git status
```

## Add Files

```bash
git add .
```

## Commit Changes

```bash
git commit -m "Initial commit - AI chatbot application"
```

## Set Main Branch

```bash
git branch -M main
```

## Add GitHub Repository

```bash
git remote add origin https://github.com/YOUR-USERNAME/chatbot1.git
```

## Verify Remote Repository

```bash
git remote -v
```

## Push Code

```bash
git push -u origin main
```

---

# Updating Code on GitHub

After making changes to the project:

```bash
git status
```

Then:

```bash
git add .
```

Commit:

```bash
git commit -m "Update chatbot application"
```

Push:

```bash
git push
```

---

# .gitignore

The project uses `.gitignore` to prevent unnecessary or sensitive files from being uploaded to GitHub.

Example:

```text
.venv/
__pycache__/
*.pyc
.env
.vercel/
**/.vercel/
```

This prevents the following from being committed:

```text
Python virtual environment
Python cache files
Environment variable files
Local Vercel configuration
```

---

# Security Practices

The project follows basic security practices.

The Ollama API key is stored only on the backend using environment variables.

The API key is not included in frontend JavaScript.

The `.env` file is excluded from Git.

Ollama API requests are made from the backend.

Users communicate with the FastAPI backend instead of directly accessing Ollama credentials.

---

# Current Application Components

```text
Frontend
HTML
CSS
JavaScript

Backend
Python
FastAPI

AI Platform
Ollama

Local Model
Llama 3.2

Cloud Model
gpt-oss:20b

Hosting
Vercel

Version Control
GitHub
```

---

# Future Enhancements

The application can be enhanced further by adding:

- Conversation history
- Chat memory
- Markdown rendering
- Streaming AI responses
- User authentication
- Google login
- Database integration
- Saved conversations
- Model selection
- RAG
- PDF upload
- Document question answering
- Rate limiting
- User-specific chat history
- Better monitoring and logging

---

# Learning Objectives

This project demonstrates how a Generative AI application works end-to-end.

```text
User Prompt
     ↓
Frontend
     ↓
REST API Call
     ↓
FastAPI
     ↓
LLM
     ↓
Generated Response
     ↓
Frontend
```

The project provides hands-on experience with Python, FastAPI, REST APIs, frontend-backend communication, LLM integration, local LLM execution, cloud LLM APIs, environment variables, API security, Vercel deployment, Git, and GitHub.

---

# Running the Complete Application - Quick Reference

Open the project:

```bash
cd chatbot1
```

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install -r backend/requirements.txt
```

Make sure Ollama is available:

```bash
ollama list
```

Start backend:

```bash
uvicorn backend.main:app --reload
```

Open another terminal.

Go to frontend:

```bash
cd frontend
```

Start frontend:

```bash
python -m http.server 5500
```

Open:

```text
http://localhost:5500
```

The application should now be ready to use.

---

# Author

Built as a hands-on Generative AI learning project using:

**Python + FastAPI + Ollama + HTML + CSS + JavaScript + Vercel + GitHub**