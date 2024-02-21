from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")


client = OpenAI()
client.api_key = api_key

# Creates the fine tuning model
client.fine_tuning.jobs.create(
    training_file="file-oqOLxl2p4tMdYnAn6X2WbICW", model="gpt-3.5-turbo"
)


# List 10 fine-tuning jobs
# print(client.fine_tuning.jobs.list(limit=10))

# List up to 10 events from a fine-tuning job
# client.fine_tuning.jobs.list_events(fine_tuning_job_id="ftjob-Bhac4EyBcw5zGuURX3kaOHRP", limit=10)

# Delete a fine-tuned model (must be an owner of the org the model was created in)
# client.models.delete("ft:gpt-3.5-turbo:acemeco:suffix:Bhac4EyBcw5zGuURX3kaOHRP")

# Cancel a job
# client.fine_tuning.jobs.cancel("ftjob-Bhac4EyBcw5zGuURX3kaOHRP")
