import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Deepgram and Fetch.ai API keys
    DEEPGRAM_API_KEY = os.getenv('DEEPGRAM_API_KEY', 'default_deepgram_key')
    FETCH_AI_API_KEY = os.getenv('FETCH_AI_API_KEY', 'default_fetchai_key')

    # Spot robot configuration
    AGENT_RPC = os.getenv('AGENT_RPC', 'ws://127.0.0.1:8888')
    OWNER_KEY = os.getenv('OWNER_KEY', '')
    USER_KEY_PATH = os.getenv('USER_KEY_PATH', '')

    # Flask settings
    ENV = os.getenv('FLASK_ENV', 'development')
    DEBUG = ENV == 'development'

    # Spot Robot network configuration
    SPOT_IP = os.getenv('SPOT_IP', '127.0.0.1')
    SPOT_PORT = int(os.getenv('SPOT_PORT', '8080'))

    SERVER_HOST = '0.0.0.0'
    SERVER_PORT = 5000
