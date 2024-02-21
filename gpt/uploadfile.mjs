// idk why i started this project with javascript - aj
// this file can be ignored

import fs from 'fs';
import fetch from 'node-fetch'; // Make sure your environment is properly set for ES modules
import { OpenAI } from 'openai'; // Adjusted import based on typical OpenAI SDK usage

const openai = new OpenAI();

openai.apiKey = '';

// Wrap the operation in an async function to use await
async function uploadAndRetrieveFileId() {
  try {
    const response = await openai.files.create({
      file: fs.createReadStream(
        '/Users/akshat/Documents/RobustPhysics-RASA-project/gpt/finetuning.jsonl'
      ),
      purpose: 'fine-tune',
    });

    // Assuming the response structure includes the file ID in a property. Adjust as necessary.
    console.log('Uploaded file ID:', response);
    return response; // Return the ID for further use
  } catch (error) {
    console.error('Failed to upload file:', error);
    throw error; // Rethrow or handle error as appropriate for your application
  }
}

uploadAndRetrieveFileId().then((fileId) => console.log('File ID:', fileId));
