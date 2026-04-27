import os
from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel
from loguru import logger


def _ensure_api_key() -> str | None:
    api_key = os.environ.get("GOOGLE_API_KEY")
    if api_key:
        return api_key
    else:
        logger.warning("No Google API key provided")
        return None


def get_google_genai_model(name:str)-> BaseChatModel:
    model = init_chat_model(name)
    return model