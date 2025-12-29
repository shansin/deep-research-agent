from agents import Agent, WebSearchTool, ModelSettings
from local_models import gpt_model
from agents import function_tool
import os
from dotenv import load_dotenv

load_dotenv(override=True)

INSTRUCTIONS = (
    "You are a research assistant. Given a search term, you search the web for that term and "
    "produce a concise summary of the results. The summary must 2-3 paragraphs and less than 300 "
    "words. Capture the main points. Write succintly, no need to have complete sentences or good "
    "grammar. This will be consumed by someone synthesizing a report, so its vital you capture the "
    "essence and ignore any fluff. Do not include any additional commentary other than the summary itself.")

#todo: get search tool selection from UI
@function_tool
def web_search_tool(search_topic: str):
    """Tool to search the web"""
    #return tavily_search(search= search_topic, max_results= 10)
    return searxng_search(search= search_topic, page_no=1)

def searxng_search(search: str, page_no: int):
    import requests
    from pprint import pprint

    endpoint = f"{os.getenv("SEARXNG_API_URL")}/search"

    params = {
        "q": search,
        "format": "json",
        "categories": "general",
        "language": "en",
        "safesearch": 0,
        "pageno": page_no
    }

    response = requests.get(endpoint, params=params, timeout=10)
    response.raise_for_status()
    results = response.json().get("results", [])
    #print(json.dumps(results, indent=4))
    return results

#tutorial https://github.com/NirDiamant/agents-towards-production/blob/main/tutorials/agent-with-tavily-web-access/search-extract-crawl.ipynb
def tavily_search(search: str, max_results: int):
    from tavily import TavilyClient
    import json
    tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    search_results = tavily_client.search(
        query=search, 
        max_results=max_results,
        time_range="week",
        include_raw_content=True,
        #include_domains=["techcrunch.com"],
        topic="news")
        
    #print(json.dumps(search_results, indent=4))
    return search_results

search_agent = Agent(
    name="SearchAgent",
    instructions=INSTRUCTIONS,
    tools=[web_search_tool],
    model=gpt_model,
    #model_settings=ModelSettings(tool_choice="required"),
)