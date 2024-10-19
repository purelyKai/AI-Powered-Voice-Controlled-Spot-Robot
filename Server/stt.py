from flask import Flask, request, jsonify
from deepgram import DeepgramClient, PrerecordedOptions
from config import Config

app = Flask(__name__)

# Initialize Deepgram client
deepgram = DeepgramClient(Config.DEEPGRAM_API_KEY)

# @app.route('/transcribe', methods=['POST'])
# def transcribe(audio_data):

        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Update port as necessary
