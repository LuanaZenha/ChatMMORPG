from typing import Dict, Set
from fastapi import WebSocket

class WSManager:
    """
    Gerencia conexões WebSocket por sala.
    - connect: aceita WS e adiciona na sala.
    - disconnect: remove WS da sala; apaga sala vazia.
    - broadcast: envia payload JSON para todos na sala.
    """
    def __init__(self) -> None:
        self.rooms: Dict[str, Set[WebSocket]] = {}

    async def connect(self, room: str, ws: WebSocket) -> None:
        await ws.accept()
        self.rooms.setdefault(room, set()).add(ws)

    def disconnect(self, room: str, ws: WebSocket) -> None:
        conns = self.rooms.get(room)
        if conns and ws in conns:
            conns.remove(ws)
            if not conns:
                self.rooms.pop(room, None)

    async def broadcast(self, room: str, payload: dict) -> None:
        """
        Envia payload para todos os sockets conectados na sala.
        Remove conexões quebradas.
        """
        for ws in list(self.rooms.get(room, [])):
            try:
                await ws.send_json(payload)
            except Exception:
                self.disconnect(room, ws)
