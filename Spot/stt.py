import asyncio
from deepgram import Deepgram

# Path to the audio file
AUDIO_FILE = "command.wav"
API_KEY = "b4ca74a0dff243508decdff556f543869eaffca2"

# Function to get text from Deepgram API
async def getText():
    try:
        # STEP 1: Create a Deepgram client using the API key
        deepgram = Deepgram(API_KEY)
        
        # Open the audio file as a binary buffer
        with open(AUDIO_FILE, "rb") as audio_file:  # Ensure the file is opened in binary mode
            buffer_data = audio_file.read()

        # STEP 2: Configure Deepgram options for audio analysis
        options = {
            "model": "nova-2",  # Ensure this is a valid model name
            "smart_format": True
        }

        # STEP 3: Call the transcribe method asynchronously
        response = await deepgram.transcription.prerecorded(
            {'buffer': buffer_data, 'mimetype': 'audio/wav'},  # Add mimetype here
            options
        )

        # STEP 4: Extract the transcript from the response
        transcript = response["results"]["channels"][0]["alternatives"][0]["transcript"]
        print(transcript)
        # Return the transcript
        return transcript

    except Exception as e:
        print(f"Exception: {e}")

# Run the async function
# if __name__ == "__main__":
#     # Since getText is async, run it with asyncio
#     asyncio.run(getText())
