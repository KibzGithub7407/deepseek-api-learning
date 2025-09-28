import requests
from python.config import Config

def generate_content(topic, content_type="blog post"):
    """
    Generate different types of content using DeepSeek API
    """
    prompt = f"Write a {content_type} about: {topic}"
    
    messages = [
        {
            "role": "system",
            "content": "You are a professional content writer. Create engaging, well-structured content."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
    
    data = {
        "model": Config.DEFAULT_MODEL,
        "messages": messages,
        "max_tokens": 2000,
        "temperature": 0.7
    }
    
    try:
        response = requests.post(Config.API_URL, headers=Config.HEADERS, json=data)
        
        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"]
        else:
            return f"Error: {response.status_code} - {response.text}"
            
    except Exception as e:
        return f"Request failed: {e}"

def main():
    """Main function for content writer"""
    print("✍️  DeepSeek Content Writer")
    print("Generate blog posts, articles, and more!")
    print("-" * 50)
    
    content_types = {
        "1": "blog post",
        "2": "article", 
        "3": "email newsletter",
        "4": "social media post",
        "5": "product description"
    }
    
    print("\nAvailable content types:")
    for key, value in content_types.items():
        print(f"  {key}. {value}")
    
    while True:
        topic = input("\n📝 Enter topic (or 'quit' to exit): ").strip()
        
        if topic.lower() == 'quit':
            print("👋 Happy writing!")
            break
        elif not topic:
            print("⚠️  Please enter a topic")
            continue
            
        type_choice = input("📋 Choose content type (1-5): ").strip()
        content_type = content_types.get(type_choice, "blog post")
        
        print(f"\n🔄 Generating {content_type} about: {topic}")
        print("-" * 50)
        
        content = generate_content(topic, content_type)
        print(content)
        print("-" * 50)

if __name__ == "__main__":
    main()
