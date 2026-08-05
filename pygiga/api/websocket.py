"""
pygiga.api.websocket
====================

WebSocket Server

Author: PyGiga
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uvicorn


class WebSocketServer:
    """
    PyGiga WebSocket Server
    """

    def __init__(
        self,
        title: str = "PyGiga WebSocket",
        version: str = "0.1.0",
    ):

        self.app = FastAPI(
            title=title,
            version=version,
        )

        self.clients = []

        self._register_routes()

    # --------------------------------------------------
    # Routes
    # --------------------------------------------------

    def _register_routes(self):

        @self.app.websocket("/ws")
        async def websocket_endpoint(
            websocket: WebSocket,
        ):

            await websocket.accept()

            self.clients.append(websocket)

            try:

                while True:

                    message = await websocket.receive_text()

                    response = {
                        "status": "success",
                        "message": message,
                    }

                    await websocket.send_json(response)

            except WebSocketDisconnect:

                if websocket in self.clients:
                    self.clients.remove(websocket)

    # --------------------------------------------------
    # Broadcast
    # --------------------------------------------------

    async def broadcast(
        self,
        message,
    ):

        disconnected = []

        for client in self.clients:

            try:

                await client.send_json(message)

            except Exception:

                disconnected.append(client)

        for client in disconnected:

            if client in self.clients:
                self.clients.remove(client)

    # --------------------------------------------------
    # Client Count
    # --------------------------------------------------

    def client_count(self):

        return len(self.clients)

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "server": "WebSocket",
            "clients": self.client_count(),
        }

    # --------------------------------------------------
    # Run
    # --------------------------------------------------

    def run(
        self,
        host: str = "0.0.0.0",
        port: int = 8001,
    ):

        uvicorn.run(
            self.app,
            host=host,
            port=port,
        )