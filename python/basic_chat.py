import requests
import json
from config import Config

def basic_chat_completion():
    """
    Basic example of DeepSeek API chat completion
    Perfect for beginners to understand API basics
    """
    print("🤖 DeepSeek API - Basic Chat Example")
    print("=" * 40)
    
    # Validate configuration
    Config.validate_config()
    
    # Request data
    data = {
        "model": Config.DEFAULT_MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful AI assistant. Provide clear, concise responses."
            },
            {
                "role": "user", 
                "content": "Hello! Can you explain what an API is in simple terms?"
            }
        ],
        "max_tokens": Config.DEFAULT_MAX_TOKENS,
        "temperature": Config.DEFAULT_TEMPERATURE,
        "stream": False
    }
    
    try:
        print("📤 Sending request to DeepSeek API...")
        
        # Make API request
        response = requests.post(
            Config.API_URL,
            headers=Config.HEADERS,
            json=data
        )
        
        # Check if request was successful
        if response.status_code == 200:
            result = response.json()
            
            # Extract and display the response
            assistant_reply = result["choices"][0]["message"]["content"]
            usage = result.get("usage", {})
            
            print("✅ Response received!")
            print("-" * 40)
            print(f"🤖 Assistant: {assistant_reply}")
            print("-" * 40)
            print(f"📊 Usage: {usage.get('prompt_tokens', 0)} prompt tokens, "
                  f"{usage.get('completion_tokens', 0)} completion tokens")
                  
        else:
            print(f"❌ Error: {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.RequestException as e:
        print(f"🚨 Request failed: {e}")
    except KeyError as e:
        print(f"🚨 Error parsing response: {e}")
    except Exception as e:
        print(f"🚨 Unexpected error: {e}")

if __name__ == "__main__":
    basic_chat_completion()
