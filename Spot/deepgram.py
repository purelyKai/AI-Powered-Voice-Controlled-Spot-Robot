from flask import Flask, request, jsonify
from Spot.deepgram import DeepgramClient, PrerecordedOptions
from Spot.config import Config

app = Flask(__name__)

# Initialize Deepgram client
deepgram = DeepgramClient(Config.DEEPGRAM_API_KEY)

@app.route('/transcribe', methods=['POST'])
def transcribe():
    # Ensure a file is provided
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']

    # Ensure the file is a valid audio file
    if not file or not file.filename.endswith('.wav'):
        return jsonify({"error": "Invalid file type, only WAV files are allowed"}), 400

    # Prepare options for Deepgram
    options = PrerecordedOptions(
        smart_format=True,
        model="nova-2",
        language="en-US"
    )

    # Transcribe the audio file
    try:
        payload = {'buffer': file.stream}
        response = deepgram.listen.prerecorded.v('1').transcribe_file(payload, options)
        transcription = response.to_json(indent=4)
        return jsonify(transcription), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Update port as necessary
