import os
import fetch_latest_info
from dotenv import load_dotenv
import asyncio
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
from openai import AsyncOpenAI

load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')

client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

set_tracing_disabled(disabled=True)

model_config = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client)

# Define the agent once
hello_agent = Agent(
    name="Assistant Agent",
    instructions="You're a helpful assistant. Always answer with the most recent known information. If you're unsure about something, say so.",
    model=model_config
)

async def main():
    print("Type 'quit' or 'exit' to quit the chat.")
    while True:
        user_input = input("Insert your prompt: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the agent.")
            break

        context = fetch_latest_info.fetch_latest_info(user_input)
        agent_result = await Runner.run(hello_agent, user_input, context=context)

        print("Agent:", agent_result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
