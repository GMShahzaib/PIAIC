import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def my_first_agent():
    print("Initializing agent...")

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a friendly assistant."},
                {"role": "user", "content": "Say Hello, world!"}
            ]
        )

        reply = response.choices[0].message.content
        print("Agent says:", reply)

    except Exception as e:
        print("Error communicating with OpenAI:", str(e))

if __name__ == "__main__":
    my_first_agent()