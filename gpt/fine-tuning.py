from openai import OpenAI
from dotenv import load_dotenv, find_dotenv, get_key

# Automatically find and load the .env file
load_dotenv(find_dotenv())

# Directly get the API key value
api_key = get_key(find_dotenv(), "OPENAI_API_KEY")


client = OpenAI()
client.api_key = api_key

# Creates the fine tuning model
# client.fine_tuning.jobs.create(
#     training_file="file-oqOLxl2p4tMdYnAn6X2WbICW", model="gpt-3.5-turbo"
# )


# List 10 fine-tuning jobs
# print(client.fine_tuning.jobs.list(limit=10))

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
        {"role": "system", "content": "I am here to help you fix your EMC models!"},
        {"role": "user", "content": prompt},
    ],
)

# Assuming you want to print the content of the first completion choice
print("")
for choice in response.choices:
    print(choice.message.content)

# # Cancel a job
# client.fine_tuning.jobs.cancel("ftjob-Bhac4EyBcw5zGuURX3kaOHRP")

# # List up to 10 events from a fine-tuning job
# client.fine_tuning.jobs.list_events(fine_tuning_job_id="ftjob-Bhac4EyBcw5zGuURX3kaOHRP", limit=10)

# # Delete a fine-tuned model (must be an owner of the org the model was created in)
# client.models.delete("ft:gpt-3.5-turbo:acemeco:suffix:Bhac4EyBcw5zGuURX3kaOHRP")
