import requests
import json
from config import Config

def test_error_scenarios():
    """
    Demonstrate various error scenarios and handling
    """
    print("🐛 DeepSeek API - Error Handling Examples")
    print("=" * 45)
    
    # Test 1: Invalid API Key
    print("\n1. Testing invalid API key...")
    test_invalid_key()
    
    # Test 2: Invalid URL
    print("\n2. Testing invalid endpoint...")
    test_invalid_endpoint()
    
    # Test 3: Malformed request
    print("\n3. Testing malformed request...")
    test_malformed_request()

def test_invalid_key():
    """Test with invalid API key"""
    invalid_headers = Config.HEADERS.copy()
    invalid_headers["Authorization"] = "Bearer invalid-key-123"
    
    data = {
        "model": Config.DEFAULT_MODEL,
        "messages": [{"role": "user", "content": "Hello"}]
    }
    
    try:
        response = requests.post(Config.API_URL, headers=invalid_headers, json=data)
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.text[:100]}...")
    except Exception as e:
        print(f"   Exception: {e}")

def test_invalid_endpoint():
    """Test with invalid API endpoint"""
    invalid_url = "https://api.deepseek.com/invalid-endpoint"
    
    data = {
        "model": Config.DEFAULT_MODEL,
        "messages": [{"role": "user", "content": "Hello"}]
    }
    
    try:
        response = requests.post(invalid_url, headers=Config.HEADERS, json=data)
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.text[:100]}...")
    except Exception as e:
        print(f"   Exception: {e}")

def test_malformed_request():
    """Test with malformed request data"""
    malformed_data = {
        "model": Config.DEFAULT_MODEL,
        # Missing required 'messages' field
        "invalid_field": "this shouldn't be here"
    }
    
    try:
        response = requests.post(Config.API_URL, headers=Config.HEADERS, json=malformed_data)
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.text[:100]}...")
    except Exception as e:
        print(f"   Exception: {e}")

def robust_chat_example():
    """
    Example of robust error handling in a chat application
    """
    print("\n🛡️  Robust Chat Example")
    print("-" * 30)
    
    messages = [
        {"role": "user", "content": "What's the weather like today?"}
    ]
    
    max_retries = 3
    for attempt in range(max_retries):
        try:
            data = {
                "model": Config.DEFAULT_MODEL,
                "messages": messages,
                "max_tokens": Config.DEFAULT_MAX_TOKENS
            }
            
            response = requests.post(
                Config.API_URL,
                headers=Config.HEADERS,
                json=data,
                timeout=30  # 30 second timeout
            )
            
            if response.status_code == 200:
                result = response.json()
                reply = result["choices"][0]["message"]["content"]
                print(f"✅ Success: {reply}")
                return reply
                
            elif response.status_code == 429:
                print("   ⚠️ Rate limited. Retrying...")
                continue
                
            else:
                print(f"   ❌ API Error {response.status_code}: {response.text}")
                break
                
        except requests.exceptions.Timeout:
            print("   ⏰ Request timeout. Retrying...")
            continue
        except requests.exceptions.ConnectionError:
            print("   🔌 Connection error. Retrying...")
            continue
        except Exception as e:
            print(f"   🚨 Unexpected error: {e}")
            break
    
    print("   💥 All retry attempts failed")

if __name__ == "__main__":
    test_error_scenarios()
    robust_chat_example()
