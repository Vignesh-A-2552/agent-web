from app.config.config import AppConfig
from langchain_openai import ChatOpenAI


def get_llm(model_name: str, temperature: float = 0)->ChatOpenAI:
    config = AppConfig()

    llm_config = {
        "model" :model_name,
        "temperature":temperature,
        "openai_api_key":config.openai_api_key
    }

    llm = ChatOpenAI(**llm_config)
    return llm