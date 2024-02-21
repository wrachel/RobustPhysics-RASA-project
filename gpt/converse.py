from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()
client.api_key = api_key

# Retrieve the state of a fine-tune
retrieve_response = client.fine_tuning.jobs.retrieve("ftjob-bNv7FO6fFX0VEYAF0tm4gQfT")

# print(retrieve_response)

print("Enter your prompt:")
prompt = input()

fine_tuned_model = retrieve_response.fine_tuned_model

# To be able to talk to the model
response = client.chat.completions.create(
    model=fine_tuned_model,
    messages=[
        {
            "role": "system",
            "content": "I am here to help you fix your EMC models through robust physics software!",
        },
        {"role": "user", "content": prompt},
    ],
)

# Assuming you want to print the content of the first completion choice
print("")
for choice in response.choices:
    print(choice.message.content)
