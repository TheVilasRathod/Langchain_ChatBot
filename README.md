# AI Assistant - Gemini Flash 2.5 Chatbot

A powerful command-line chatbot built with LangChain and Google's Gemini Flash 2.5 model, featuring conversation memory and enhanced user experience.

## Features

- 🤖 **Gemini Flash 2.5 Integration** - Latest Google AI model
- 💭 **Conversation Memory** - Remembers last 5 exchanges
- ⚡ **Real-time Responses** - Fast and efficient processing
- 🛡️ **Error Handling** - Robust error management
- 🎯 **Simple Commands** - Easy-to-use interface

## Quick Start

### Prerequisites

- Python 3.8+
- Google AI API Key

### Installation

1. **Clone/Download** the project
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment:**
   Create a `.env` file:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

4. **Run the chatbot:**
   ```bash
   python app.py
   ```

## Usage

### Commands
- Type any question and press Enter
- `clear` - Clear conversation history
- `help` - Show help message
- `exit` - Quit application

### Example Session
```
🙋 You: What is machine learning?
🤖 Assistant: Machine learning is a subset of artificial intelligence...

🙋 You: Give me an example
🤖 Assistant: Based on our previous discussion about machine learning...
```

## Configuration

### Model Settings
- **Model:** `gemini-2.0-flash-exp`
- **Temperature:** 0.7 (balanced creativity)
- **Max Tokens:** 1024
- **Memory:** Last 5 exchanges

### Customization
Modify these parameters in `app.py`:
```python
self.llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    temperature=0.7,  # Adjust creativity (0-1)
    max_tokens=1024,  # Response length
    timeout=30        # Request timeout
)
```

## Project Structure
```
simple_QA_model/
├── app.py              # Main application
├── requirements.txt    # Dependencies
├── .env               # API key (create this)
└── README.md          # Documentation
```

## Dependencies

- **langchain** - LLM framework
- **langchain-google-genai** - Gemini integration
- **python-dotenv** - Environment variables

## Troubleshooting

### Common Issues

**API Key Error:**
```
🔴 Error: GOOGLE_API_KEY not found
```
- Ensure `.env` file exists with valid API key

**Import Error:**
```bash
pip install --upgrade langchain langchain-google-genai
```

**Connection Issues:**
- Check internet connection
- Verify API key is active

## License

MIT License - Feel free to modify and distribute.

---

**Built with ❤️ using LangChain and Google Gemini**