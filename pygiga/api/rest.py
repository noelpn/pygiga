"""
pygiga.api.rest
===============

REST API Server

Author: PyGiga
"""

from typing import Any, Dict

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn


class RESTServer:
    """
    REST API Server
    """

    def __init__(
        self,
        title: str = "PyGiga API",
        version: str = "0.1.0",
    ):

        self.app = FastAPI(
            title=title,
            version=version,
        )

        self._register_routes()

    # --------------------------------------------------
    # Routes
    # --------------------------------------------------

    def _register_routes(self):

        @self.app.get("/")
        async def home():

            return {
                "framework": "PyGiga",
                "status": "running",
                "version": "0.1.0",
            }

        @self.app.get("/health")
        async def health():

            return {
                "status": "healthy"
            }

        @self.app.post("/run")
        async def run(
            payload: Dict[str, Any]
        ):

            return JSONResponse(
                {
                    "received": payload,
                    "status": "success",
                }
            )

    # --------------------------------------------------
    # Run Server
    # --------------------------------------------------

    def run(
        self,
        host: str = "0.0.0.0",
        port: int = 8000,
    ):

        uvicorn.run(
            self.app,
            host=host,
            port=port,
        )

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "server": "REST",
            "framework": "FastAPI",
        }