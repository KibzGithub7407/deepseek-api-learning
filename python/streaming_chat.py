import requests
import json
from config import Config

def streaming_chat_completion():
    """
    Example of streaming chat completion
    Shows real-time response generation
    """
    print("🌊 DeepSeek API - Streaming Chat Example")
    print("=" * 45)
    
    # Request data with streaming enabled
    data = {
        "model": Config.DEFAULT_MODEL,
        "messages": [
            {
                "role": "user",
                "content": "Tell me a short story about a programmer learning APIs"
            }
        ],
        "max_tokens": 500,
        "temperature": 0.8,
        "stream": True
    }
    
    try:
        print("📤 Starting streaming request...")
        print("-" * 45)
        
        # Make streaming request
        response = requests.post(
            Config.API_URL,
            headers=Config.HEADERS,
            json=data,
            stream=True
        )
        
        if response.status_code == 200:
            print("🤖 Assistant: ", end="", flush=True)
            
            # Process streaming response
            for line in response.iter_lines():
                if line:
                    line = line.decode('utf-8')
                    if line.startswith('data: '):
                        data_str = line[6:]  # Remove 'data: ' prefix
                        
                        if data_str == '[DONE]':
                            print("\n" + "-" * 45)
                            print("✅ Stream completed!")
                            break
                            
                        try:
                            data_json = json.loads(data_str)
                            if 'choices' in data_json and data_json['choices']:
                                delta = data_json['choices'][0].get('delta', {})
                                if 'content' in delta:
                                    print(delta['content'], end="", flush=True)
                        except json.JSONDecodeError:
                            continue
            print()  # New line at the end
            
        else:
            print(f"❌ Error: {response.status_code}")
            print(f"Response: {response.text}")
            
    except Exception as e:
        print(f"🚨 Error: {e}")

if __name__ == "__main__":
    streaming_chat_completion()
