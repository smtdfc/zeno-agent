from pydantic.dataclasses import dataclass


@dataclass
class ChatModelConfig:
    temperature: float
    batch_size: int
    timeout: float
    max_tokens: int
    max_retries: int

@dataclass
class Config:
    model: ChatModelConfig
