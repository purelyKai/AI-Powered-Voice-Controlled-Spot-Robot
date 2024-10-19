from flask import Flask, request, jsonify
import deepgram
import fetch_ai
#from spot_control.spot_interface import SpotInterface
from config import Config

app = Flask(__name__)

# Initialize the Spot interface
#spot = SpotInterface(Config.SPOT_IP, Config.SPOT_PORT)

@app.route('/transcribe', methods=['POST'])
def transcribe_voice():
    """Handle voice input from Spot, send to Deepgram, and process it."""
    # Get voice data from the request
    voice_data = request.files.get('voice')
    if not voice_data:
        return jsonify({'error': 'No voice data received'}), 400

    # Call Deepgram to transcribe the voice input
    transcript = deepgram.transcribe(voice_data)
    
    # Send the transcript to Fetch.ai for processing
    response = fetch_ai.process_text(transcript)
    
    # Return the result
    return jsonify({'response': response})

@app.route('/spot/command', methods=['POST'])
def send_spot_command():
    """Receive a command and send it to the Spot robot."""
    data = request.json
    command = data.get('command')
    
    if not command:
        return jsonify({'error': 'No command provided'}), 400
    
    # Execute the command on the Spot robot
    #result = spot.execute_command(command)
    result = 0
    
    return jsonify({'status': 'success', 'result': result})

if __name__ == '__main__':
    app.run(host=Config.SERVER_HOST, port=Config.SERVER_PORT, debug=Config.DEBUG)
