import subprocess
import json
import sys

article_title = "AgentCraft AI: An Open-Source Multi-Agent Workspace Powered by Open-Weight LLMs"

body_markdown = """---
title: AgentCraft AI: An Open-Source Multi-Agent Workspace Powered by Open-Weight LLMs
published: false
tags: devchallenge, hf26challenge, hacktoberfest, ai
---

*This article is a submission for the [Hacktoberfest Open-Source AI Challenge: Week 1](https://dev.to/challenges/hacktoberfest-week1-2026-10-05).*

---

### 🌟 Inspiration & Background

Building with AI shouldn't require sending private codebase architecture or sensitive developer documentation to proprietary cloud APIs. 

With the rapid advancement of **open-weight AI models** (such as Google's Gemma 2, Meta's Llama 3, and local runtime tools like Ollama and Hugging Face Transformers), developers now have the power to run high-performance AI agents completely offline on local hardware.

I created **AgentCraft AI** — a lightweight, modular multi-agent framework designed to orchestrate specialized AI agents for code auditing, documentation synthesis, and project planning, all powered by open-weight AI.

---

### ✨ What It Does

**AgentCraft AI** provides three specialized developer agents:

1. 🏗️ **Code Architect Agent**: Inspects code structure, identifies methods/classes, audits security risks, and suggests architectural refactoring.
2. 📑 **Docs Summarizer Agent**: Chunks and synthesizes lengthy technical specifications or API docs into executive summaries and bullet points.
3. 🎯 **Task Planner Agent**: Decomposes high-level developer goals into step-by-step implementation milestones and generates dynamic Mermaid workflow diagrams.

---

### 🏗️ Architecture & Multi-Agent Flow

```mermaid
flowchart TD
    User["Developer"] -->|Submits Code / Task Goal| AgentCraft["AgentCraft AI Workspace"]
    AgentCraft --> Architect["Code Architect Agent"]
    AgentCraft --> Summarizer["Docs Summarizer Agent"]
    AgentCraft --> Planner["Task Planner Agent"]
    
    Architect -->|Local Inference| OpenWeightLLM["Open-Weight LLM (Gemma 2 / Llama 3 / Ollama)"]
    Summarizer -->|Local Inference| OpenWeightLLM
    Planner -->|Local Inference| OpenWeightLLM
    
    OpenWeightLLM -->|Parsed Output| Results["Structured JSON & Mermaid Diagrams"]
    Results --> User
```

---

### 💻 Open-Source Code & Setup

The project is 100% open-source under the **MIT License**.

* 📂 **GitHub Repository**: [samainakhatun115-cpu/agentcraft-ai](https://github.com/samainakhatun115-cpu/agentcraft-ai)
* 🚀 **Tech Stack**: Python 3.9+, Open-Weight Models (Gemma 2 / Ollama / Hugging Face), Standard JSON Parsers.

#### Running AgentCraft AI:

```python
from app import AgentCraft

# Initialize Workspace with an open-weight model engine
framework = AgentCraft(model_name="Gemma-2B / Llama-3-OpenWeight")

# 1. Run Code Architect Agent
code_analysis = framework.architect_agent(code_snippet)

# 2. Run Docs Summarizer Agent
summary = framework.summarizer_agent(doc_text)

# 3. Run Task Planner Agent
plan = framework.planner_agent("Deploy Local AI Code Auditor")
```

---

### 🎯 Hacktoberfest 2026: AI Belongs to Everyone

Hacktoberfest 2026's central mission — *"AI belongs to everyone"* — highlights the crucial role of open-source models and toolings. By running multi-agent workflows with open-weight models, developers maintain complete privacy, transparency, and freedom from vendor lock-in.

---

### 🚀 What's Next

* 🌐 Web UI Dashboard built with Streamlit / Gradio.
* 🛠️ Agentic Function Calling & Local File System Execution.
* 💬 Local Chat Interface for interactive Q&A.

Thank you for reading, and happy Hacktoberfest! 🎃✨
"""

payload = {
    "article": {
        "title": article_title,
        "body_markdown": body_markdown,
        "published": False,
        "tags": ["devchallenge", "hf26challenge", "hacktoberfest", "ai"]
    }
}

payload_json = json.dumps(payload)

cmd = [
    r"C:\Users\DELL\.devrelay\bin\dev_mlh_mcp_server.exe",
    "api",
    "POST",
    "/api/articles",
    "{}",
    payload_json
]

try:
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    print("SUCCESS: Staged DEV Week 1 draft successfully!")
    print(res.stdout)
except subprocess.CalledProcessError as e:
    print("ERROR staging draft:", e.returncode)
    print("Stdout:", e.stdout)
    print("Stderr:", e.stderr)
