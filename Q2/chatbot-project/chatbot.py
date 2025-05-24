import chainlit as cl
from my_secrets import Secrets
from agents import Agent, Runner, AsyncOpenAI, set_default_openai_api, set_tracing_disabled, OpenAIChatCompletionsModel

@cl.on_message
async def handle_user_input(user_msg: cl.Message):
    config = Secrets()
    llm_client = AsyncOpenAI(
        api_key=config.get_api_key(),
        base_url=config.get_api_base_url()
    )

    set_tracing_disabled(True)
    set_default_openai_api(llm_client)

    assistant = Agent(
        name="AI Assistant",
        instructions="Provide the most accurate answer you can.",
        model=OpenAIChatCompletionsModel(
            model=config.get_api_model(),
            openai_client=llm_client
        )
    )

    response = Runner.run_sync(
        starting_agent=assistant,
        input=user_msg.content
    )

    reply = cl.Message(content=response.final_output)
    await reply.send()
