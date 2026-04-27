from os import path
from pathlib import Path

from pydantic import TypeAdapter

from core.settings.setting import Setting
from core.configs.app_storage import config_dir


def save_setting(setting: Setting) -> None:
    adapter = TypeAdapter(Setting)
    json_string = adapter.dump_json(setting).decode("utf-8")
    Path(path.join(config_dir, "settings.json")).write_text(
        json_string, encoding="utf-8")


def load_setting() -> Setting:
    file_path = Path(path.join(config_dir, "settings.json"))

    if not file_path.exists():
        return Setting(
            models={},
            currentModelSelect=None
        )

    json_data = file_path.read_bytes()
    adapter = TypeAdapter(Setting)
    setting = adapter.validate_json(json_data)

    return setting
