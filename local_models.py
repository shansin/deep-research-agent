import os
from agents import OpenAIChatCompletionsModel
from agents import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

client = AsyncOpenAI(base_url=os.getenv("OLLAMA_BASE_URL"), api_key="ollama")

gpt_model = OpenAIChatCompletionsModel(model="gpt-oss:20b", openai_client=client)
llama_model = OpenAIChatCompletionsModel(model="llama3.1:8b", openai_client=client)
deepseek_model = OpenAIChatCompletionsModel(model="deepseek-r1:8b", openai_client=client)