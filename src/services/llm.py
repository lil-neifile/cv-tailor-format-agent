import logging

from langchain.tools import BaseTool
from langchain_core.messages import AIMessage
from langchain_litellm import ChatLiteLLM
import litellm
from pydantic import BaseModel

from config import config

logger = logging.getLogger(__name__)


def get_llm(max_tokens: int|None=None, model: str|None=config.MODEL_PRIMARY) -> ChatLiteLLM:
    logger.info(f"Getting LLM for model: {model}")
    return ChatLiteLLM(
        model=model,
        api_key=config.LLM_API_KEY,
        max_tokens=max_tokens,
        temperature=0.2,
        reasoning_effort="minimal",
        request_timeout=20,
        max_retries=2
)

def invoke_structured(schema: BaseModel, system: str, user: str, max_tokens: int) -> BaseModel:
    logger.info(f"Invoking structured output for schema: {schema}")
    messages=[
        
        {"role": "system", "content": system},
        {"role": "user", "content": user}
    ]

    try:
        llm = get_llm(max_tokens)
        structured = llm.with_structured_output(schema)
        result = structured.invoke(messages)
        return result   
    except (litellm.Timeout, litellm.RateLimitError, litellm.APIConnectionError, litellm.APIError):
        logger.exception(f"Error calling primary LLM, calling backup")
        llm = get_llm(max_tokens, config.MODEL_BACKUP)
        structured = llm.with_structured_output(schema)
        result = structured.invoke(messages)


def invoke_chat(system, user, max_tokens: int|None=None) -> AIMessage:
    logger.info(f"Invoking chat for system")
    messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": user}
    ]
    llm = get_llm(max_tokens)
    try:
        return llm.invoke(messages)
    except (litellm.Timeout, litellm.RateLimitError, litellm.APIConnectionError, litellm.APIError):
        logger.exception(f"Error calling primary LLM, calling backup")
        llm = get_llm(max_tokens, config.MODEL_BACKUP)
        return llm.invoke(messages)
        
def get_llm_with_tools(tools: list[BaseTool]) -> ChatLiteLLM:
    logger.info(f"Getting LLM with tools: {tools}")
    llm = get_llm()
    try: 
        return llm.bind_tools(tools)
    except (litellm.Timeout, litellm.RateLimitError, litellm.APIConnectionError, litellm.APIError):
        logger.warning(f"Error calling primary LLM, calling backup")
        llm = get_llm(config.MODEL_BACKUP)
        return llm.bind_tools(tools)
