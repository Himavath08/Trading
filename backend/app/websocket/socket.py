from fastapi import APIRouter, WebSocket
from app.services.websocket_manager import manager

router = APIRouter()

@router.websocket("/ws")

async def websocket_endpoint(
    websocket: WebSocket
):

    await manager.connect(websocket)

    try:

        while True:

            data = await websocket.receive_text()

            await manager.send_message(
                f"Message: {data}"
            )

    except:

        manager.disconnect(websocket)