import os
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

class Settings:
    """
    Centraliza configurações do app.
    Use get_settings() para obter a instância única.
    """
    def __init__(self) -> None:
        self.MONGO_URL: str = os.getenv("MONGO_URL", "")
        self.MONGO_DB: str = os.getenv("MONGO_DB", "chatdb")
        self.APP_HOST: str = os.getenv("APP_HOST", "0.0.0.0")
        self.APP_PORT: int = int(os.getenv("APP_PORT", "8000"))

_settings: Settings | None = None

def get_settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings
