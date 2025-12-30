# 🔍 Deep Research Agent

A powerful, multi-agent autonomous research system that performs in-depth investigations into any topic. It coordinates multiple specialized AI agents to plan research, search the web, synthesize findings, and deliver professional reports directly to your inbox.

## 🌟 Features

- **Multi-Agent Orchestration**: Specialized agents for planning, searching, writing, and delivery.
- **Local Model Support**: Optimized for local execution using **Ollama** (supports llama3.1, deepseek-r1, etc.).
- **Autonomous Web Research**: Plans and executes multiple targeted web searches using **Tavily**.
- **Professional Reporting**: Generates structured Markdown reports with citations and insights.
- **Immediate Delivery**: Sends finished reports via **Resend** (Email) and provides status updates via **Pushover** (Mobile).
- **Interactive UI**: Clean, responsive interface built with **Gradio**.

---

## 🤖 The Agent Team

The system operates using four specialized agents coordinated by the `ResearchManager`:

1.  **Planner Agent**: Analyzes the research topic and breaks it down into a comprehensive search strategy and multiple specific queries.
2.  **Search Agent**: Executes the planned searches, filtering and extracting the most relevant information from the web.
3.  **Writer Agent**: Synthesizes search results into a cohesive, detailed, and well-structured professional report.
4.  **Email Agent**: Converts the final report into clean HTML and handles reliable delivery to your specified email.

---

## 🛠️ Tech Stack

- **Core Framework**: [OpenAI Agents SDK](https://github.com/openai/openai-agents-python)
- **Interface**: [Gradio](https://gradio.app/)
- **Package Management**: [uv](https://github.com/astral-sh/uv)
- **Web Search**: [SearXNG](https://docs.searxng.org/) or [Tavily API](https://tavily.com/)
- **Email Service**: [Resend](https://resend.com/)
- **Notifications**: [Pushover](https://pushover.net/)
- **Local LLM Server**: [Ollama](https://ollama.com/)

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.12 or higher.
- [uv](https://github.com/astral-sh/uv) installed (`powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`).
- (Optional) [Ollama](https://ollama.com/) for local model support.

### 2. Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/your-username/deep-research-agent.git
cd deep-research-agent
uv sync
```

### 3. Configuration
Create a `.env` file in the root directory (using `.env _example` as a template):
```env
OPENAI_API_KEY=your_openai_key  # Optional if using local models exclusively
TAVILY_API_KEY=your_tavily_key # Optional if using SearXNG exclusively
RESEND_API_KEY=your_resend_key
PUSHOVER_USER=your_pushover_user
PUSHOVER_TOKEN=your_pushover_token

# Search Config
SEARCH_PROVIDER=searxng        # Options: "searxng" (default) or "tavily" 
SEARXNG_API_URL="http://localhost:8081"
TAVILY_API_KEY=your_tavily_key

# Local Model Config
OLLAMA_BASE_URL="http://localhost:11434/v1"

# Email Config
FROM_NAME="Deep Research"
FROM_EMAIL="research@yourdomain.com"
TO_EMAIL="your@email.com"
```

### 4. Running the Agent
Start the Gradio web interface:
```bash
uv run deep_research.py
```
After running, open your browser to the local URL (usually `http://127.0.0.1:7860`).

---

## 📈 Monitoring & Debugging
This project uses **OpenAI Traces** for observability. When you start a research task, a trace URL will be generated. You can use this to monitor the step-by-step logic and communication between agents in real-time.

---

## 📝 License
MIT License. See [LICENSE](LICENSE) for details.
