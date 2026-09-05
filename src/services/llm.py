from langchain_litellm import ChatLiteLLM
import litellm
from pydantic import BaseModel
import logging
from langchain_core.messages import AIMessage
from langchain.tools import BaseTool
from config import model_primary, model_backup, llm_api_key


def get_llm(max_tokens: int|None=None, model: str|None=model_primary) -> ChatLiteLLM:
    return ChatLiteLLM(
        model=model,
        api_key=llm_api_key,
        max_tokens=max_tokens,
        temperature=0.2,
        reasoning_effort="minimal",
        request_timeout=10,
        max_retries=1
)

def invoke_structured(schema: BaseModel, system: str, user: str, max_tokens: int) -> BaseModel:
    messages=[
        
        {"role": "system", "content": system},
        {"role": "user", "content": user}
    ]

    try:
        llm = get_llm(max_tokens)
        structured = llm.with_structured_output(schema)
        result = structured.invoke(messages)

    except (litellm.Timeout, litellm.RateLimitError, litellm.APIConnectionError, litellm.APIError):
        logging.warning(f"Error calling primary LLM, calling backup")
        llm = get_llm(max_tokens, model_backup)
        structured = llm.with_structured_output(schema)
        result = structured.invoke(messages)
    return result

def invoke_chat(system, user, max_tokens: int|None=None) -> AIMessage:
    messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": user}
    ]
    llm = get_llm(max_tokens)
    try:
        return llm.invoke(messages)
    except (litellm.Timeout, litellm.RateLimitError, litellm.APIConnectionError, litellm.APIError):
        logging.warning(f"Error calling primary LLM, calling backup")
        llm = get_llm(max_tokens, model_backup)
        return llm.invoke(messages)
def get_llm_with_tools(tools: list[BaseTool]) -> ChatLiteLLM:
    llm = get_llm()
    try: 
        return llm.bind_tools(tools)
    except (litellm.Timeout, litellm.RateLimitError, litellm.APIConnectionError, litellm.APIError):
        logging.warning(f"Error calling primary LLM, calling backup")
        llm = get_llm(model_backup)
        return llm.bind_tools(tools)
