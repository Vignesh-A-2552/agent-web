from pydantic import BaseModel, Field

class AppConfig(BaseModel):
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")