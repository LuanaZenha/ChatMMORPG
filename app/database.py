from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from datetime import datetime, timezone
from app.config import get_settings

_client: Optional[AsyncIOMotorClient] = None

def get_db() -> AsyncIOMotorDatabase:
    """
    Retorna uma instância do banco do MongoDB.
    Inicializa o cliente de forma lazy (apenas no primeiro uso).
    Lança erro se MONGO_URL não estiver definido.
    """
    global _client
    settings = get_settings()

    if not settings.MONGO_URL:
        raise RuntimeError("Defina MONGO_URL no .env (string do MongoDB Atlas).")

    if _client is None:
        _client = AsyncIOMotorClient(settings.MONGO_URL)

    return _client[settings.MONGO_DB]

def ensure_aware(dt: datetime) -> datetime:
    """
    Garante que um datetime seja timezone-aware em UTC.
    """
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt
