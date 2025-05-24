import os
import chainlit as cl
import json
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

# Load .env variables
load_dotenv()

# Set the API key explicitly in the client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Store conversation
conversation_history = []

@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content
    conversation_history.append({"role": "user", "content": user_input})

    # OpenAI completion call
    response = client.chat.completions.create(
        model="gpt-4",
        messages=conversation_history
    )
    
    bot_response = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": bot_response})

    await cl.Message(content=bot_response).send()

@cl.on_stop
async def save_chat_history():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"chat_history_{timestamp}.json"
    with open(file_name, "w") as f:
        json.dump(conversation_history, f, indent=2)
