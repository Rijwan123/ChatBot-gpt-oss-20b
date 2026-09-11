# AI Assistant using FastAPI, Ollama and Vercel

A full-stack Generative AI chatbot application built using **Python, FastAPI, Ollama, HTML, CSS, JavaScript, Vercel, Git, and GitHub**.

The application supports two execution modes:

- **Local Development:** Runs `llama3.2:latest` using Ollama installed locally.
- **Cloud / Production:** Runs `gpt-oss:20b` using Ollama Cloud and a FastAPI backend deployed on Vercel.

---

## Live Application

You can access the deployed AI Assistant here:

[Open AI Assistant](https://chatbotfrontend-omega.vercel.app/)

## Application Preview

[![AI Assistant Application](images\image.png)]


> The application frontend and backend are hosted on Vercel, and AI responses are generated using Ollama Cloud with the `gpt-oss:20b` model.


```

> The backend URL is mainly for development and API testing. Normal users should use the frontend application URL.

---

# Project Overview

This project demonstrates how to build and deploy a complete Generative AI application consisting of:

- Frontend user interface
- Python backend
- REST API
- Large Language Model integration
- Local LLM execution
- Cloud LLM execution
- Vercel deployment
- GitHub source-code management

The user enters a question in the web interface.

The frontend sends the question to the FastAPI backend.

The backend communicates with Ollama.

Ollama processes the request using the configured Large Language Model and returns the generated response.

---

# Application Flow

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

# Project Structure

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

# Features

- Generative AI chatbot interface
- Python FastAPI backend
- REST API integration
- Ollama local model support
- Ollama Cloud support
- Local and cloud execution modes
- Responsive frontend
- User and AI message bubbles
- Loading animation while AI generates a response
- Enter key support for sending messages
- Error handling
- Environment-variable-based production configuration
- API key protection
- Vercel frontend deployment
- Vercel backend deployment
- Git and GitHub source control

---

# Technology Stack

| Component | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python |
| API Framework | FastAPI |
| LLM Platform | Ollama |
| Local Development Model | `llama3.2:latest` |
| Production Cloud Model | `gpt-oss:20b` |
| Frontend Hosting | Vercel |
| Backend Hosting | Vercel |
| Source Control | Git & GitHub |

---

# Models Used

The application supports two different models depending on where it is running.

| Mode | Model | Purpose |
|---|---|---|
| Local Development | `llama3.2:latest` | Runs locally through Ollama |
| Cloud / Production | `gpt-oss:20b` | Runs through Ollama Cloud |

---

## Local Development Model

When the application is running locally and `OLLAMA_API_KEY` is not available, the FastAPI backend uses:

```text
llama3.2:latest
```

The model runs through Ollama installed on the developer's computer.

Architecture:

```text
Frontend
   ↓
FastAPI
   ↓
Local Ollama
   ↓
llama3.2:latest
   ↓
AI Response
```

---

## Production Cloud Model

When `OLLAMA_API_KEY` is available, the backend automatically switches to Ollama Cloud.

The currently configured production model is:

```text
gpt-oss:20b
```

Architecture:

```text
Vercel Frontend
      ↓
Vercel FastAPI Backend
      ↓
Ollama Cloud
      ↓
gpt-oss:20b
      ↓
AI Response
```

---

# Prerequisites

Before running the application locally, install:

- Python
- Ollama
- Git
- VS Code or another code editor

---

# Check Python Installation

Open PowerShell, Command Prompt, or the VS Code terminal.

Run:

```bash
python --version
```

Example:

```text
Python 3.12.x
```

---

# Check Ollama Installation

Run:

```bash
ollama --version
```

If Ollama is installed correctly, its version will be displayed.

---

# Check Git Installation

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

## Step 1 - Clone the Repository

Clone the GitHub repository:

```bash
git clone https://github.com/YOUR-USERNAME/chatbot1.git
```

Go inside the project:

```bash
cd chatbot1
```

If the project already exists on your computer, you can skip this step.

---

# Step 2 - Create a Python Virtual Environment

From the project root directory:

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

After activation, the terminal should show:

```text
(.venv)
```

---

# Step 3 - Install Python Dependencies

Run:

```bash
python -m pip install -r backend/requirements.txt
```

The main Python packages used are:

```text
fastapi
uvicorn
httpx
ollama
```

---

# Step 4 - Download the Local Ollama Model

Download Llama 3.2:

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

# Step 5 - Test Ollama

Run:

```bash
ollama run llama3.2
```

Ask:

```text
What is Generative AI?
```

If Ollama generates an answer, the local model is working correctly.

To exit:

```text
/bye
```

---

# Step 6 - Start the FastAPI Backend

From the root project directory run:

```bash
uvicorn backend.main:app --reload
```

The backend will start at:

```text
http://127.0.0.1:8000
```

You should see:

```text
Uvicorn running on http://127.0.0.1:8000
```

---

# Step 7 - Test the Backend

Open:

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

# Step 8 - Open FastAPI Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

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

# Step 9 - Run the Frontend

Keep the backend terminal running.

Open another terminal.

Go to the frontend directory:

```bash
cd frontend
```

Start the frontend server:

```bash
python -m http.server 5500
```

Open:

```text
http://localhost:5500
```

The AI Assistant interface should appear.

---

# Local Development Architecture

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
llama3.2:latest
        ↓
AI Response
```

---

# How Local and Cloud Mode Are Selected

The FastAPI backend checks for:

```text
OLLAMA_API_KEY
```

If `OLLAMA_API_KEY` is not available:

```text
Local Mode
   ↓
Ollama installed locally
   ↓
llama3.2:latest
```

If `OLLAMA_API_KEY` is available:

```text
Cloud Mode
   ↓
Ollama Cloud
   ↓
gpt-oss:20b
```

This allows the same backend application to support both local development and cloud deployment.

---

# Local Configuration

No `.env` file is used in this project.

For local development:

```text
OLLAMA_API_KEY is not configured
        ↓
Backend detects local mode
        ↓
Local Ollama is used
        ↓
llama3.2:latest
```

Therefore, the local application can run without configuring cloud credentials.

---

# Ollama Cloud Configuration

The production application uses environment variables configured directly in Vercel.

The required production variables are:

```text
OLLAMA_API_KEY
OLLAMA_MODEL
```

The production model is configured as:

```text
OLLAMA_MODEL=gpt-oss:20b
```

The variables are configured directly in:

```text
Vercel
→ Project
→ Settings
→ Environment Variables
```

No `.env` file is required for the deployed application.

---

# API Key Security

Never hard-code the Ollama API key inside Python code.

Do not use:

```python
api_key = "my-secret-api-key"
```

Instead, the backend reads the key from the Vercel environment:

```python
api_key = os.getenv("OLLAMA_API_KEY")
```

The actual API key is securely stored in Vercel and is not part of the GitHub repository.

The frontend must never contain the Ollama API key.

---

# Backend API Endpoints

## Home Endpoint

```http
GET /
```

Purpose:

Verify that the backend is running.

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

Example production response:

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

This endpoint retrieves the Ollama models available through the configured Ollama Cloud account.

It is mainly useful for development and troubleshooting.

---

# Frontend to Backend Communication

The frontend sends the user's message to the FastAPI backend using JavaScript.

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

The frontend communicates only with FastAPI.

It does not directly communicate with Ollama Cloud.

This prevents the Ollama API key from being exposed to users.

---

# Production Architecture

```text
User
  ↓
Vercel Frontend
  ↓
HTML + CSS + JavaScript
  ↓
HTTPS POST Request
  ↓
Vercel FastAPI Backend
  ↓
OLLAMA_API_KEY
  ↓
Ollama Cloud
  ↓
gpt-oss:20b
  ↓
Generated AI Response
  ↓
FastAPI
  ↓
Frontend
  ↓
User
```

---

# Deployment

Both the frontend and backend are deployed separately on Vercel.

## Frontend Deployment

```text
HTML
CSS
JavaScript
    ↓
Vercel
```

The frontend provides the user interface.

---

## Backend Deployment

```text
Python
FastAPI
    ↓
Vercel
    ↓
Ollama Cloud
    ↓
gpt-oss:20b
```

The backend securely handles communication with Ollama Cloud.

---

# Environment Variables

The production backend uses environment variables configured directly in Vercel.

| Variable | Purpose |
|---|---|
| `OLLAMA_API_KEY` | Authenticates the backend with Ollama Cloud |
| `OLLAMA_MODEL` | Defines the cloud model |

Current production model:

```text
gpt-oss:20b
```

For local development, these cloud environment variables are not required.

---

# GitHub

GitHub is used to store and manage the project source code.

The application itself is hosted on Vercel.

```text
GitHub
   ↓
Source Code Repository


Vercel
   ↓
Frontend + Backend Hosting


Ollama Cloud
   ↓
gpt-oss:20b
```

Users access the application using the Vercel frontend URL.

Developers can access the source code through GitHub.

---

# Git Commands

## Initialize Repository

```bash
git init
```

---

## Check Git Status

```bash
git status
```

---

## Add Files

```bash
git add .
```

---

## Commit Files

```bash
git commit -m "Initial commit - AI chatbot application"
```

---

## Set Main Branch

```bash
git branch -M main
```

---

## Add GitHub Remote

```bash
git remote add origin https://github.com/YOUR-USERNAME/chatbot1.git
```

---

## Verify Remote

```bash
git remote -v
```

---

## Push to GitHub

For the first push:

```bash
git push -u origin main
```

For future pushes:

```bash
git push
```

---

# Updating the Project on GitHub

After modifying the application:

Check changes:

```bash
git status
```

Add changes:

```bash
git add .
```

Commit changes:

```bash
git commit -m "Update chatbot application"
```

Push changes:

```bash
git push
```

---

# .gitignore

The project uses `.gitignore` to prevent unnecessary or potentially sensitive files from being committed.

Recommended `.gitignore`:

```text
.venv/
__pycache__/
*.pyc
.env
.vercel/
**/.vercel/
```

The project currently does **not** use a `.env` file.

The `.env` entry is included only as a safety precaution so that if a `.env` file is created in the future, it will not accidentally be committed to GitHub.

The `.gitignore` prevents items such as:

- Python virtual environment
- Python cache files
- Future `.env` files
- Local Vercel configuration

from being committed.

---

# Security Practices

The project follows basic security practices:

- Ollama API key is stored securely in Vercel Environment Variables.
- API keys are not hard-coded in Python.
- API keys are not exposed in frontend JavaScript.
- No `.env` file containing credentials is used.
- Ollama Cloud communication happens through the FastAPI backend.
- Users communicate with FastAPI rather than directly with Ollama Cloud.
- Sensitive Vercel configuration is excluded from Git.

---

# Current Application Components

```text
Frontend
├── HTML
├── CSS
└── JavaScript

Backend
├── Python
└── FastAPI

AI Platform
└── Ollama

Local Development Model
└── llama3.2:latest

Production Cloud Model
└── gpt-oss:20b

Hosting
└── Vercel

Source Control
├── Git
└── GitHub
```

---

# Quick Start

For developers who already have Python and Ollama installed:

## 1. Clone Repository

```bash
git clone https://github.com/YOUR-USERNAME/chatbot1.git
```

## 2. Enter Project

```bash
cd chatbot1
```

## 3. Create Virtual Environment

```bash
python -m venv .venv
```

## 4. Activate Virtual Environment

```bash
.venv\Scripts\activate
```

## 5. Install Dependencies

```bash
python -m pip install -r backend/requirements.txt
```

## 6. Download Local Model

```bash
ollama pull llama3.2
```

## 7. Start Backend

```bash
uvicorn backend.main:app --reload
```

## 8. Open Another Terminal

```bash
cd frontend
```

## 9. Start Frontend

```bash
python -m http.server 5500
```

## 10. Open Application

```text
http://localhost:5500
```

---

# Future Enhancements

Possible future improvements include:

- Conversation history
- Chat memory
- Markdown rendering
- Streaming AI responses
- User authentication
- Google login
- Microsoft login
- Database integration
- Save previous conversations
- User-specific chat history
- Model selection
- Retrieval-Augmented Generation (RAG)
- PDF upload
- Document question answering
- Rate limiting
- API usage monitoring
- Better logging
- Improved exception handling
- Dynamic model selection
- Admin dashboard

---

# Learning Objectives

This project provides hands-on experience with:

- Python programming
- FastAPI
- REST API development
- Frontend development
- Backend development
- Frontend-backend communication
- Generative AI
- Large Language Models
- Ollama
- Local LLM execution
- Cloud LLM APIs
- Environment variables
- API security
- Vercel deployment
- Git
- GitHub

---

# End-to-End Learning Flow

```text
User Prompt
     ↓
Frontend
     ↓
JavaScript
     ↓
HTTP REST API
     ↓
FastAPI
     ↓
Ollama
     ↓
Large Language Model
     ↓
Generated Response
     ↓
Frontend
     ↓
User
```

---

# Summary

This project demonstrates a complete full-stack Generative AI chatbot architecture.

## Local Development

```text
Frontend
→ FastAPI
→ Local Ollama
→ llama3.2:latest
```

No `.env` file or cloud API key is required for local mode.

## Production

```text
Vercel Frontend
→ Vercel FastAPI Backend
→ Ollama Cloud
→ gpt-oss:20b
```

Production credentials and model configuration are stored directly in Vercel Environment Variables.

## Source Control

```text
Git
→ GitHub
```

This setup allows the application to be developed locally using a locally running LLM while also supporting cloud deployment for public access.

---

# Author

Built as a hands-on Generative AI learning project using:

**Python + FastAPI + Ollama + HTML + CSS + JavaScript + Vercel + GitHub**