from langchain_litellm import ChatLiteLLM
import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic import BaseModel
import logging


ROOT = Path(__file__).resolve().parents[3]
load_dotenv(ROOT / ".env")
load_dotenv(ROOT  / "../.env")

llm_api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("MODEL")

def get_llm(max_tokens: int|None=None) -> ChatLiteLLM:
    return ChatLiteLLM(
        model=model,
        api_key=llm_api_key,
        max_tokens=max_tokens,
        temperature=0.2,
        reasoning_effort="minimal"
)


def invoke_structured(schema: BaseModel, system: str, user: str, max_tokens: int) -> dict:
    messages=[
        
        {"role": "system", "content": system},
        {"role": "user", "content": user}
    ]

    llm = get_llm(max_tokens)


    try:
        structured = llm.with_structured_output(schema)
        result = structured.invoke(messages)
        if isinstance(result, schema):
            return result
        return schema.model_validate(result)
    except Exception:
        logging.exception(f"Error invoking structured output")
        raise

def invoke_chat(system, user, max_tokens: int|None=None) -> dict:
    messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": user}
    ]
    llm = get_llm(max_tokens)
    return llm.invoke(messages)