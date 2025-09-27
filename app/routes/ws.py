from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from datetime import datetime, timezone
from app.database import get_db
from app.models import MessageIn, serialize_mongo
from app.manager import WSManager

router = APIRouter(tags=["ws"])
manager = WSManager()

@router.websocket("/ws/{room}")
async def ws_room(ws: WebSocket, room: str):
    """
    WebSocket da sala.
    Envia histórico inicial e transmite novas mensagens para todos da sala.
    """
    await manager.connect(room, ws)
    try:
        cursor = get_db()["messages"].find({"room": room}).sort("_id", -1).limit(20)
        items = [serialize_mongo(d) async for d in cursor]
        items.reverse()
        await ws.send_json({"type": "history", "items": items})

        while True:
            payload = await ws.receive_json()
            try:
                data = MessageIn.model_validate({
                    "username": payload.get("username", "anon"),
                    "content": payload.get("content", ""),
                })
            except Exception:

                continue

            doc = {
                "room": room,
                "username": data.username,
                "content": data.content,
                "created_at": datetime.now(timezone.utc),
            }
            res = await get_db()["messages"].insert_one(doc)
            doc["_id"] = res.inserted_id
            await manager.broadcast(room, {"type": "message", "item": serialize_mongo(doc)})
    except WebSocketDisconnect:
        manager.disconnect(room, ws)
