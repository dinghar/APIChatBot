from fastapi import FastAPI
from dotenv import load_dotenv
import os
import openai
from models.chat_request import ChatRequest
from testData import testChat

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Success"}

@app.post("/chat")
def chat(chatRequest: ChatRequest):
    # Pass OpenAPI spec, user request, and prompt to LLM.
    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        # Use hardcoded test data for now
        messages=testChat,
    )
    message = completions.choices[0].text.strip()

    # TODO: Parse response to get the formatted request

    # TODO: Make request to API

    # TODO: Log request and response to later train LLM

    # TODO: Return response to user

    return {"message": "TODO"}

