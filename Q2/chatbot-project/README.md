# 🤖 Chatbot with Chainlit & OpenAI Agent SDK

This project is a conversational chatbot using Chainlit for UI and OpenAI's Agent SDK for conversation logic.

## 📷 Screenshot
![Chatbot Screenshot](screenshot.png)

## 🚀 Features

- Web-based chat interface
- AI-powered responses
- Automatically saves chat history to JSON

## 📁 Chat History

Upon ending a session, chat is saved as `chat_history_YYYYMMDD_HHMMSS.json` with user messages and bot responses.

## 💻 Setup

```bash
pip install -r requirements.txt
chainlit run main.py
