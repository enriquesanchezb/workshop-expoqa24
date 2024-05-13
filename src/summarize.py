from langchain_community.llms import Ollama

from prompt.summary import prompt as summary_template
from src.prompt_helper import execute_prompt, generate_prompt


def summarize(text: str, llm: str = "phi3") -> str:
    """Summarize a text."""

    llm = Ollama(model=llm)
    system_message_prompt_template = summary_template["systemMessagePromptTemplate"]
    human_prompt_template = summary_template["humanPromptTemplate"]
    prompt = generate_prompt(
        system_message_prompt_template, human_prompt_template, text
    )

    output = execute_prompt(llm, prompt, text)
    return output
