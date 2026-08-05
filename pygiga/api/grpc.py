"""
pygiga.api.grpc
===============

gRPC Server

Author: PyGiga
"""

from concurrent import futures
import grpc


class GRPCServer:
    """
    Generic gRPC server wrapper.
    """

    def __init__(
        self,
        host: str = "0.0.0.0",
        port: int = 50051,
        workers: int = 10,
    ):

        self.host = host
        self.port = port

        self.server = grpc.server(
            futures.ThreadPoolExecutor(
                max_workers=workers
            )
        )

        self.services = []

    # -----------------------------------------
    # Register
    # -----------------------------------------

    def register_service(
        self,
        registration_function,
        service,
    ):
        """
        Register a generated gRPC service.

        Example:
            add_PyGigaServicer_to_server(
                PyGigaService(),
                server
            )
        """

        registration_function(
            service,
            self.server,
        )

        self.services.append(service)

    # -----------------------------------------
    # Start
    # -----------------------------------------

    def start(self):

        address = f"{self.host}:{self.port}"

        self.server.add_insecure_port(address)

        self.server.start()

        print(f"gRPC server running on {address}")

    # -----------------------------------------
    # Wait
    # -----------------------------------------

    def wait(self):

        self.server.wait_for_termination()

    # -----------------------------------------
    # Stop
    # -----------------------------------------

    def stop(self, grace: int = 0):

        self.server.stop(grace)

    # -----------------------------------------
    # Information
    # -----------------------------------------

    def info(self):

        return {
            "host": self.host,
            "port": self.port,
            "services": len(self.services),
        }