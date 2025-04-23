# src/llm_commenter.py

from openai import OpenAI

MODEL = "llama3.2"
client = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')


def generate_comments(architecture_text: str, prompt_template: str) -> str:
    """
    Sends the architecture description and prompt to the LLM, returns the generated comments.
    """
    prompt = prompt_template.replace("{ARCHITECTURE_TEXT}", architecture_text)
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
    )
    return response.choices[0].message.content


def generate_full_report(architecture_text: str, prompt_template: str) -> str:
    """
    Combines the original architecture description and the LLM-generated comments
    into a formatted markdown-style report.
    """
    comments = generate_comments(architecture_text, prompt_template)
    full_report = f"""\
📄 **Architecture Description**
------------------------------
{architecture_text}

🧠 **LLM-Generated Review**
------------------------------
{comments}
"""
    return full_report
