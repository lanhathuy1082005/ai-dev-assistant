from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-3.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are a senior developer assistant. Be direct and concise."
    ),
    contents=[
        types.Content(role="user", parts=[types.Part(text="What is a REST API?")]),
        types.Content(role="user", parts=[types.Part(text="Give me a one line example use case.")])
    ]
)

print(response.text)