"""
pygiga.action.robotics
======================

Generic Robotics Action Module

Author: PyGiga
"""

from typing import Dict


class RoboticsAction:
    """
    Generic robotics interface.
    """

    def __init__(self):

        self.connected = False
        self.robot_name = "Unknown Robot"

    # --------------------------------------------------
    # Connection
    # --------------------------------------------------

    def connect(self, robot_name: str = "PyGiga Robot") -> bool:
        """
        Connect to a robot.
        """

        self.connected = True
        self.robot_name = robot_name

        return True

    def disconnect(self) -> bool:
        """
        Disconnect from robot.
        """

        self.connected = False

        return True

    # --------------------------------------------------
    # Movement
    # --------------------------------------------------

    def move_forward(self, distance: float):
        return f"Moving forward {distance} meter(s)"

    def move_backward(self, distance: float):
        return f"Moving backward {distance} meter(s)"

    def turn_left(self, angle: float):
        return f"Turning left {angle} degrees"

    def turn_right(self, angle: float):
        return f"Turning right {angle} degrees"

    def stop(self):
        return "Robot stopped"

    # --------------------------------------------------
    # Arm Control
    # --------------------------------------------------

    def pick(self, object_name: str):
        return f"Picking {object_name}"

    def place(self, location: str):
        return f"Placing object at {location}"

    # --------------------------------------------------
    # Sensors
    # --------------------------------------------------

    def sensors(self) -> Dict:

        return {
            "camera": True,
            "microphone": True,
            "lidar": False,
            "gps": False,
            "temperature": 25.0,
        }

    # --------------------------------------------------
    # Status
    # --------------------------------------------------

    def battery(self) -> int:
        return 100

    def info(self):

        return {
            "connected": self.connected,
            "robot": self.robot_name,
            "battery": self.battery(),
            "sensors": self.sensors(),
        }

    # --------------------------------------------------
    # Emergency
    # --------------------------------------------------

    def emergency_stop(self):

        self.connected = False

        return "Emergency Stop Activated"