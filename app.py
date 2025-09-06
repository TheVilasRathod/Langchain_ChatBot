import os
import sys
from datetime import datetime
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.memory import ConversationBufferWindowMemory
from langchain.schema import HumanMessage, AIMessage

class ChatBot:
    def __init__(self):
        self.llm = None
        self.chain = None
        self.memory = ConversationBufferWindowMemory(
            k=5,  # Keep last 5 exchanges
            return_messages=True
        )
        
    def initialize(self):
        """Initialize the chatbot components"""
        try:
            # Load environment variables
            load_dotenv()
            
            # Validate API key
            if not os.getenv("GOOGLE_API_KEY"):
                print("🔴 Error: GOOGLE_API_KEY not found.")
                print("Please create a .env file and add your GOOGLE_API_KEY.")
                return False
            
            print("🚀 Initializing AI Assistant with Gemini Flash 2.5...")
            
            # Initialize LLM with better configuration
            self.llm = ChatGoogleGenerativeAI(
                model="gemini-2.0-flash-exp",
                temperature=0.7,
                max_tokens=1024,
                timeout=30
            )
            
            # Create enhanced prompt template with conversation history
            prompt = ChatPromptTemplate.from_messages([
                ("system", "You are a helpful, knowledgeable, and friendly AI assistant. "
                          "Provide clear, accurate, and concise responses. "
                          "Consider the conversation history when responding."),
                ("human", "{question}")
            ])
            
            # Build the chain
            self.chain = prompt | self.llm | StrOutputParser()
            
            print("✅ Assistant ready! Enhanced with conversation memory.")
            return True
            
        except Exception as e:
            print(f"🔴 Initialization error: {str(e)}")
            return False
    
    def get_response(self, question):
        """Get response from the chatbot with error handling"""
        try:
            # Get conversation history
            history = self.memory.chat_memory.messages
            
            # Create context with history
            context = ""
            if history:
                context = "\nConversation history:\n"
                for msg in history[-4:]:  # Last 2 exchanges
                    if isinstance(msg, HumanMessage):
                        context += f"Human: {msg.content}\n"
                    elif isinstance(msg, AIMessage):
                        context += f"Assistant: {msg.content}\n"
                context += "\nCurrent question:\n"
            
            full_question = context + question if context else question
            
            # Get response
            response = self.chain.invoke({"question": full_question})
            
            # Save to memory
            self.memory.chat_memory.add_user_message(question)
            self.memory.chat_memory.add_ai_message(response)
            
            return response
            
        except Exception as e:
            return f"❌ Error generating response: {str(e)}"
    
    def print_welcome(self):
        """Print welcome message with instructions"""
        print("\n" + "="*50)
        print("🤖 AI Assistant - Powered by Gemini Flash 2.5")
        print("="*50)
        print("Commands:")
        print("  • Type your question and press Enter")
        print("  • 'clear' - Clear conversation history")
        print("  • 'help' - Show this help message")
        print("  • 'exit' - Quit the application")
        print("="*50)
    
    def run(self):
        """Main chat loop"""
        if not self.initialize():
            return
        
        self.print_welcome()
        
        while True:
            try:
                user_input = input("\n🙋 You: ").strip()
                
                if not user_input:
                    continue
                
                # Handle commands
                if user_input.lower() == "exit":
                    print("\n👋 Thank you for using AI Assistant. Goodbye!")
                    break
                elif user_input.lower() == "clear":
                    self.memory.clear()
                    print("🧹 Conversation history cleared.")
                    continue
                elif user_input.lower() == "help":
                    self.print_welcome()
                    continue
                
                # Get and display response
                print("\n🤖 Assistant: ", end="", flush=True)
                response = self.get_response(user_input)
                print(response)
                
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Unexpected error: {str(e)}")

def main():
    """Entry point for the application"""
    chatbot = ChatBot()
    chatbot.run()

if __name__ == "__main__":
    main()