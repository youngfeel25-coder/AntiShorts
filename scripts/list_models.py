import os
from google import genai
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

try:
    for m in client.models.list():
        print(m.name)
except Exception as e:
    print(f"Error: {e}")
