import os
from typing import Dict
import requests
from agents import Agent, function_tool
from local_models import gpt_model
from dotenv import load_dotenv
load_dotenv(override=True)

@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """Send an email with the given subject and HTML body"""
    # from_email has to be configured on dns, xxx@shanup.com is enabled
    to = [os.getenv("TO_EMAIL")]
    from_name = os.getenv("FROM_NAME")
    from_email = os.getenv('FROM_EMAIL')

    headers = {
        "Authorization": f"Bearer {os.getenv("RESEND_API_KEY")}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "from": f"{from_name} <{from_email}>",
        "to": to,
        "subject": subject,
        "html": html_body
    }
    
    # Send email using Resend API
    response = requests.post("https://api.resend.com/emails", json=payload, headers=headers)
    
    # Check if the request was successful
    if response.ok:
        return {"status": "success"}
    else:
        return {"status": "failure", "message": response.text}


INSTRUCTIONS = """You are able to send a nicely formatted HTML email based on a detailed report.
You will be provided with a detailed report. You should use your tool to send one email, providing the 
report converted into clean, well presented HTML with an appropriate subject line."""

email_agent = Agent(
    name="EmailAgent",
    instructions=INSTRUCTIONS,
    tools=[send_email],
    model=gpt_model
)
