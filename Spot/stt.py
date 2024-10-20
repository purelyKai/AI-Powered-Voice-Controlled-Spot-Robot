from deepgram import DeepgramClient, PrerecordedOptions, FileSource

# Path to the audio file
AUDIO_FILE = "command.wav"
API_KEY = "b4ca74a0dff243508decdff556f543869eaffca2"
def getText():
    try:
        # STEP 1 Create a Deepgram client using the API key
        deepgram = DeepgramClient(API_KEY)
        with open(AUDIO_FILE, "rb") as file:
            buffer_data = file.read()
        payload: FileSource = {
            "buffer": buffer_data,
        }
        #STEP 2: Configure Deepgram options for audio analysis
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
        )
        # STEP 3: Call the transcribe_file method with the text payload and options
        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
        # STEP 4: Print the response
        transcript = response["results"]["channels"][0]["alternatives"][0]["transcript"]

        # Print the transcript
        return transcript
    except Exception as e:
        print(f"Exception: {e}")
