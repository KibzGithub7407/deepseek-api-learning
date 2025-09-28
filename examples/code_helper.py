import requests
from python.config import Config

def ask_code_question(question):
    """
    Ask coding-related questions to DeepSeek API
    """
    messages = [
        {
            "role": "system",
            "content": "You are an expert programming assistant. Provide clear, practical code examples and explanations."
        },
        {
            "role": "user",
            "content": question
        }
    ]
    
    data = {
        "model": Config.DEFAULT_MODEL,
        "messages": messages,
        "max_tokens": 1500,
        "temperature": 0.2
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
    """Main function for code helper"""
    print("💻 DeepSeek Code Helper")
    print("Ask any programming question!")
    print("Type 'quit' to exit")
    print("-" * 50)
    
    while True:
        question = input("\n❓ Your question: ").strip()
        
        if question.lower() == 'quit':
            print("👋 Happy coding!")
            break
        elif not question:
            print("⚠️  Please enter a question")
            continue
            
        print("\n🤖 Answer:")
        print("-" * 40)
        answer = ask_code_question(question)
        print(answer)
        print("-" * 40)

if __name__ == "__main__":
    main()
