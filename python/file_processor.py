import requests
import json
from config import Config

def process_file_content(file_path):
    """
    Read file content and send to DeepSeek API for processing
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        print(f"📁 Processing file: {file_path}")
        print(f"📄 Content length: {len(content)} characters")
        
        # Prepare the prompt
        messages = [
            {
                "role": "system",
                "content": "You are a helpful code and text analyzer. Provide insights and summaries."
            },
            {
                "role": "user",
                "content": f"Please analyze this content and provide a summary:\n\n{content}"
            }
        ]
        
        data = {
            "model": Config.DEFAULT_MODEL,
            "messages": messages,
            "max_tokens": 1000,
            "temperature": 0.3
        }
        
        response = requests.post(Config.API_URL, headers=Config.HEADERS, json=data)
        
        if response.status_code == 200:
            result = response.json()
            analysis = result["choices"][0]["message"]["content"]
            
            print("✅ Analysis completed!")
            print("-" * 50)
            print(analysis)
            print("-" * 50)
            
            return analysis
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
            return None
            
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return None
    except Exception as e:
        print(f"🚨 Error processing file: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    file_to_process = "example.txt"  # Change this to your file path
    process_file_content(file_to_process)
