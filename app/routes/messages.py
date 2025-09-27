from fastapi import APIRouter, HTTPException, Query
from bson import ObjectId, errors as bson_errors
from datetime import datetime, timezone
from app.database import get_db
from app.models import MessageIn, MessageOut, serialize_mongo

router = APIRouter(prefix="/rooms", tags=["messages"])

@router.get("/{room}/messages")
async def get_messages(
    room: str,
    limit: int = Query(20, ge=1, le=100),
    before_id: str | None = Query(None, description="Retorna mensagens anteriores a este _id"),
):
    """
    Lista mensagens de uma sala com paginação por cursor (_id).
    Se before_id for inválido, retorna 400.
    """
    query: dict = {"room": room}
    if before_id is not None:
        try:
            query["_id"] = {"$lt": ObjectId(before_id)}
        except (bson_errors.InvalidId, TypeError):
            raise HTTPException(status_code=400, detail="before_id inválido")

    cursor = get_db()["messages"].find(query).sort("_id", -1).limit(limit)
    docs = [serialize_mongo(d) async for d in cursor]
    docs.reverse()

    next_cursor = docs[0]["_id"] if docs else None
    # Usa MessageOut para garantir formato consistente de saída
    items = [MessageOut.model_validate(d).model_dump(by_alias=True) for d in docs]
    return {"items": items, "next_cursor": next_cursor}

@router.post("/{room}/messages", response_model=MessageOut, status_code=201)
async def post_message(room: str, payload: MessageIn):
    """
    Cria nova mensagem após validação Pydantic.
    Bloqueia conteúdo vazio (validação do modelo).
    """
    doc = {
        "room": room,
        "username": payload.username,
        "content": payload.content,
        "created_at": datetime.now(timezone.utc),
    }
    res = await get_db()["messages"].insert_one(doc)
    doc["_id"] = res.inserted_id
    return MessageOut.model_validate(serialize_mongo(doc))
