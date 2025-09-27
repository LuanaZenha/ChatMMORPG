from pydantic import BaseModel, Field, field_validator
from typing import Any
from datetime import datetime, timezone
from bson import ObjectId


class MessageIn(BaseModel):
    """
    Modelo de entrada de mensagem (validação do payload).
    """
    username: str = Field(..., min_length=1, max_length=50)
    content: str = Field(..., min_length=1, max_length=1000)

    @field_validator("username", mode="before")
    @classmethod
    def strip_username(cls, v: str) -> str:
        return str(v).strip()

    @field_validator("content", mode="before")
    @classmethod
    def strip_content(cls, v: str) -> str:
        return str(v).strip()

class MessageOut(BaseModel):
    """
    Modelo de saída de mensagem (resposta para o cliente).
    """
    id: str = Field(..., alias="_id")
    room: str
    username: str
    content: str
    created_at: datetime

    class Config:
        populate_by_name = True
        json_encoders = {
            datetime: lambda dt: (dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)).isoformat()
        }


def serialize_mongo(doc: dict[str, Any]) -> dict[str, Any]:
    """
    Converte um documento Mongo em dict serializável (strings/ISO).
    - _id -> str
    - created_at -> ISO 8601 (mantendo tzinfo)
    """
    d = dict(doc)
    if "_id" in d and isinstance(d["_id"], ObjectId):
        d["_id"] = str(d["_id"])
    if "created_at" in d and isinstance(d["created_at"], datetime):
        dt = d["created_at"]
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        d["created_at"] = dt
    return d
