from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import requests
import random

app = FastAPI()

# Hugging Face API details
HF_API_URL = "https://api-inference.huggingface.co/models/gpt2"  # Change if needed
HF_HEADERS = {"Authorization": "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"}  # Replace with actual key

# Candidate Information Model
class CandidateInfo(BaseModel):
    full_name: str
    email: str
    phone: str
    years_of_experience: int
    desired_position: str
    current_location: str
    tech_stack: List[str]

# Sample question templates
QUESTION_TEMPLATES = {
    "python": ["🐍 What are Python decorators?", "📌 Explain list vs tuple."],
    "ml": ["🤖 What is overfitting?", "📊 Explain supervised vs unsupervised learning."],
    "fastapi": ["⚡ How does FastAPI handle validation?", "🔗 Explain dependency injection in FastAPI."],
    "mongodb": ["💾 What is sharding?", "🗄️ Explain SQL vs NoSQL."],
    "react": ["⚛️ What is the virtual DOM?", "🌀 Explain React Hooks."]
}

def generate_questions(tech_stack):
    questions = []
    for tech in tech_stack:
        if tech.lower() in QUESTION_TEMPLATES:
            questions.extend(random.sample(QUESTION_TEMPLATES[tech.lower()], k=2))
    return questions

def generate_ai_response(prompt: str):
    """Generates a response using Hugging Face's GPT model"""
    try:
        response = requests.post(HF_API_URL, json={"inputs": prompt}, headers=HF_HEADERS)
        response_json = response.json()
        
        # Handle API errors
        if "error" in response_json:
            raise HTTPException(status_code=500, detail=f"Hugging Face API error: {response_json['error']}")

        return response_json[0]['generated_text'] if isinstance(response_json, list) else response_json
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch AI response: {str(e)}")

@app.post("/collect_info")
def collect_info(candidate: CandidateInfo):
    questions = generate_questions(candidate.tech_stack)

    if not questions:
        raise HTTPException(status_code=400, detail="No valid questions generated for given tech stack")

    return {"candidate": candidate.dict(), "questions": questions}

@app.post("/ask_ai")
def ask_ai(question: str):
    ai_response = generate_ai_response(question)
    return {"question": question, "ai_response": ai_response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

