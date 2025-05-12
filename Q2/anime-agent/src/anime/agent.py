import os
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, set_default_openai_api, set_tracing_disabled
from dotenv import load_dotenv
      
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

my_client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

set_default_openai_api(my_client)
set_tracing_disabled(True)

my_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=my_client
)

def run_anime_agent():
    anime_agent = Agent(
        name="AnimeBuddy",
        instructions="""
        You are AnimeBuddy, a knowledgeable and enthusiastic guide to anime.
        Help users discover anime series, explain anime terminology, genres, and popular culture.
        Always provide clear, engaging answers, and suggest anime tailored to users' preferences enthusiastically!
        """,
        model=my_model
    )
    
    prompt = "Can you explain what 'isekai' anime is and recommend some popular examples?"

    result = Runner.run_sync(anime_agent, prompt)

    with open("AnimeAioutput.md", "a", encoding="utf-8") as file:
        file.write(f"### Prompt:\n{prompt}\n\n")
        file.write(f"### Response:\n{result.final_output}\n\n---\n\n")

    print(f"Prompt: {prompt}")
    print(f"Response: {result.final_output}")
