from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(
    base_url="https://api.cerebras.ai/v1",
    api_key=os.environ.get("CEREBRAS_API_KEY") 
)

class PromptRequest(BaseModel):
    content: str

@app.post("/generate-flashcards")
async def generate_flashcards(request: PromptRequest):
    try:
        response = client.chat.completions.create(
            model="qwen-3-235b-a22b-instruct-2507",
            messages=[
                {"role": "system", "content": "Return only a JSON array of objects with 'question' and 'answer' fields."},
                {"role": "user", "content": f"Create flashcards for these notes: {request.content}"}
            ]
        )
        return {"flashcards": response.choices[0].message.content}
    except Exception as e:
        if "429" in str(e):
            raise HTTPException(status_code=429, detail="NotebookLM/API limit reached. Please try again tomorrow.")
        raise HTTPException(status_code=500, detail=str(e))
