import os
from typing import  cast

from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel, BaseLanguageModel
from langchain_core.runnables import RunnableSerializable, Runnable
from loguru import logger

from core.models.config import ChatModelConfig


def _ensure_api_key() -> str | None:
    api_key = os.environ.get("GOOGLE_API_KEY")
    if api_key:
        return api_key
    else:
        logger.warning("No Google API key provided")
        return None


def get_google_genai_model(name:str, config: ChatModelConfig)-> BaseChatModel:
    _ensure_api_key()
    model = init_chat_model(
        model_provider="google_genai",
        model_name=name,
        temperature=config.temperature,
        max_tokens=config.max_tokens,
        timeout=config.timeout,
        max_retries=config.max_retries,
    )

    return cast(BaseChatModel, cast(Runnable, model))