from pydantic import BaseModel, Field
from agents import Agent
from local_models import gpt_model
from agents import OpenAIChatCompletionsModel
import os
from openai import AsyncOpenAI


INSTRUCTIONS = f"You are a helpful research assistant. Given a query and number of searches to perform, come up with a set of web searches \
to perform to best answer the query. Do not exceed user provided number of searches"


class WebSearchItem(BaseModel):
    reason: str = Field(description="Your reasoning for why this search is important to the query.")
    query: str = Field(description="The search term to use for the web search.")


class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="A list of web searches to perform to best answer the query.")
    
planner_agent = Agent(
    name="PlannerAgent",
    instructions=INSTRUCTIONS,
    model=gpt_model,
    output_type=WebSearchPlan,
)