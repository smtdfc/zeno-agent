from pydantic.dataclasses import dataclass


@dataclass
class ModelSetting:
    provider: str
    name: str
    apiKey: str
