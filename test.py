from google import genai
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Create client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Test request
response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="Hello"
)

print(response.text)