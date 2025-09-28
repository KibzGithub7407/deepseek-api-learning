import requests
import json
from python.config import Config

class SimpleChatBot:
    """
    A simple chatbot using DeepSeek API
    Great for learning API integration patterns
    """
    
    def __init__(self):
        self.conversation_history = [
            {
                "role": "system", 
                "content": "You are a helpful and friendly assistant. Keep responses concise and engaging."
            }
        ]
        
    def chat(self, user_input):
        """
        Send user input to DeepSeek API and get response
        """
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        # Prepare request data
        data = {
            "model": Config.DEFAULT_MODEL,
            "messages": self.conversation_history,
            "max_tokens": Config.DEFAULT_MAX_TOKENS,
            "temperature": Config.DEFAULT_TEMPERATURE
        }
        
        try:
            # Make API request
            response = requests.post(
                Config.API_URL,
                headers=Config.HEADERS,
                json=data
            )
            
            if response.status_code == 200:
                result = response.json()
                assistant_reply = result["choices"][0]["message"]["content"]
                
                # Add assistant reply to history
                self.conversation_history.append({
                    "role": "assistant",
                    "content": assistant_reply
                })
                
                return assistant_reply
            else:
                return f"Error: {response.status_code} - {response.text}"
                
        except Exception as e:
            return f"Request failed: {e}"
    
    def print_conversation(self):
        """Print the entire conversation history"""
        print("\n💬 Conversation History:")
        print("=" * 50)
        for msg in self.conversation_history:
            if msg["role"] == "user":
                print(f"👤 You: {msg['content']}")
            elif msg["role"] == "assistant":
                print(f"🤖 Bot: {msg['content']}")
        print("=" * 50)

def main():
    """Main function to run the chatbot"""
    print("🤖 Simple DeepSeek ChatBot")
    print("Type 'quit' to exit, 'history' to see conversation, 'clear' to reset")
    print("-" * 60)
    
    bot = SimpleChatBot()
    
    while True:
        user_input = input("\n👤 You: ").strip()
        
        if user_input.lower() == 'quit':
            print("👋 Goodbye!")
            break
        elif user_input.lower() == 'history':
            bot.print_conversation()
            continue
        elif user_input.lower() == 'clear':
            bot = SimpleChatBot()
            print("🔄 Conversation cleared!")
            continue
        elif not user_input:
            print("⚠️  Please enter a message")
            continue
            
        print("🤖 Bot: ", end="", flush=True)
        response = bot.chat(user_input)
        print(response)

if __name__ == "__main__":
    main()
