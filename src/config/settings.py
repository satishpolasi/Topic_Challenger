import os
from dotenv import load_dotenv

load_dotenv()

class Settings():
    
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')
    
    MODEL_NAME = "llama-3.1-8b-instant"
    
    TEMPERATURE = 0.9 # Higher values mean less coherent but more creative output
    
    MAX_RETRIES = 3 # number of retries for failed requests (API)
    
settings = Settings()  # Create an instance of the Settings class
