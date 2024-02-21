import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()
client.api_key = api_key

file = client.files.create(
    file=open(
        "/Users/akshat/Documents/RobustPhysics-RASA-project/gpt/finetuning2.jsonl", "rb"
    ),
    purpose="fine-tune",
)

print(file)
print('File ID: ' + file.id)
