import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for DeepSeek API"""
    
    # API Settings
    API_KEY = os.getenv('DEEPSEEK_API_KEY', 'sk-demo-1234567890abcdef')
    API_URL = os.getenv('DEEPSEEK_API_URL', 'https://api.deepseek.com/chat/completions')
    
    # Model Settings
    DEFAULT_MODEL = os.getenv('DEFAULT_MODEL', 'deepseek-chat')
    DEFAULT_MAX_TOKENS = int(os.getenv('MAX_TOKENS', '2048'))
    DEFAULT_TEMPERATURE = float(os.getenv('TEMPERATURE', '0.7'))
    
    # Headers
    HEADERS = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    @classmethod
    def validate_config(cls):
        """Validate that required configuration is present"""
        if cls.API_KEY.startswith('sk-demo-'):
            print("⚠️  Warning: Using demo API key. Replace with your actual key in .env file")
            return False
        return True
