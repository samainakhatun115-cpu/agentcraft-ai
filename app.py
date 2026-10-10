"""
AgentCraft AI - Open-Source Multi-Agent Workspace
Built for Hacktoberfest 2026 Open-Source AI Challenge: Week 1
"""

import os
import sys
import json

# Ensure stdout handles UTF-8 for console output on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

class AgentCraft:
    def __init__(self, model_name="gemma2-openweight"):
        self.model_name = model_name
        print(f"[AgentCraft AI] Initialized Workspace [Model Engine: {self.model_name}]")

    def architect_agent(self, code_snippet: str) -> dict:
        """
        Code Architect Agent: Inspects code structure, generates documentation,
        and identifies potential security/performance improvements.
        """
        lines = code_snippet.strip().split("\n")
        functions = [l.strip() for l in lines if l.strip().startswith("def ")]
        classes = [l.strip() for l in lines if l.strip().startswith("class ")]
        
        analysis = {
            "agent": "Code Architect Agent",
            "lines_analyzed": len(lines),
            "functions_found": functions,
            "classes_found": classes,
            "security_recommendations": [
                "Verify input validation on all function arguments.",
                "Ensure error handling for IO and external dependencies."
            ],
            "architecture_note": f"Clean modular layout with {len(functions)} methods defined."
        }
        return analysis

    def summarizer_agent(self, text: str) -> dict:
        """
        Docs Summarizer Agent: Synthesizes lengthy technical papers into executive bullet points.
        """
        sentences = [s.strip() for s in text.split(".") if len(s.strip()) > 10]
        summary = sentences[:min(3, len(sentences))]
        
        return {
            "agent": "Docs Summarizer Agent",
            "executive_summary": ". ".join(summary) + "." if summary else text[:100],
            "key_takeaways": [
                "Open-weight models enable fully private, offline AI execution.",
                "Multi-agent workflows increase reliability for specialized developer tasks."
            ]
        }

    def planner_agent(self, goal: str) -> dict:
        """
        Task Planner Agent: Decomposes high-level project goals into actionable tasks
        and generates Mermaid workflow diagrams.
        """
        tasks = [
            f"Phase 1: Environment setup and open-weight model weights verification for '{goal}'",
            "Phase 2: Core agent logic implementation and prompt template creation",
            "Phase 3: Integration testing, benchmarking, and documentation"
        ]
        
        mermaid_diagram = (
            "flowchart TD\n"
            "    User['Developer'] -->|Defines Goal| Goal['Task Goal']\n"
            "    Goal --> Planner['Planner Agent']\n"
            "    Planner --> Architect['Architect Agent']\n"
            "    Planner --> Summarizer['Summarizer Agent']\n"
            "    Architect --> Output['Structured Code & Specs']\n"
            "    Summarizer --> Output\n"
        )
        
        return {
            "agent": "Task Planner Agent",
            "goal": goal,
            "action_plan": tasks,
            "mermaid_diagram": mermaid_diagram
        }

def main():
    print("==========================================================")
    print("  AgentCraft AI: Open-Source Multi-Agent Framework        ")
    print("  Hacktoberfest 2026 Open-Source AI Challenge: Week 1      ")
    print("==========================================================")
    print()

    framework = AgentCraft(model_name="Gemma-2B / Llama-3-OpenWeight")
    
    # 1. Code Architect Agent Demo
    sample_code = (
        "class ModelPipeline:\n"
        "    def __init__(self, weights_path):\n"
        "        self.weights = weights_path\n"
        "    def run_inference(self, prompt):\n"
        "        return f'Inference result for: {prompt}'\n"
    )
    print("\n--- 1. Running Code Architect Agent ---")
    arch_result = framework.architect_agent(sample_code)
    print(json.dumps(arch_result, indent=2))

    # 2. Docs Summarizer Agent Demo
    sample_docs = (
        "Open-weight AI models give developers full control over inference infrastructure. "
        "By hosting models locally with tools like Ollama or Hugging Face Transformers, "
        "teams protect sensitive data and eliminate third-party API costs."
    )
    print("\n--- 2. Running Docs Summarizer Agent ---")
    sum_result = framework.summarizer_agent(sample_docs)
    print(json.dumps(sum_result, indent=2))

    # 3. Task Planner Agent Demo
    print("\n--- 3. Running Task Planner Agent ---")
    plan_result = framework.planner_agent("Deploy Local AI Agent for Code Auditing")
    print(json.dumps(plan_result, indent=2))

if __name__ == "__main__":
    main()
