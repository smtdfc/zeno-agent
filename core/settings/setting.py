from pydantic.dataclasses import dataclass

from core.settings.model import ModelSetting


@dataclass
class Setting:
    models: dict[str, ModelSetting]
    currentModelSelect: str | None
