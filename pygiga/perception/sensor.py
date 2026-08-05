"""
pygiga.perception.sensor
========================

Sensor perception module for PyGiga.

Provides a generic interface for reading and processing
data from physical or virtual sensors.
"""

from datetime import datetime
from typing import Any, Callable, Dict, List


class SensorPerception:
    """
    Generic sensor perception interface.
    """

    def __init__(self):
        self._sensors: Dict[str, Callable] = {}

    def register(
        self,
        name: str,
        callback: Callable,
    ) -> None:
        """
        Register a sensor callback.

        Example
        -------
        sensor.register(
            "temperature",
            lambda: 26.5
        )
        """
        self._sensors[name] = callback

    def unregister(
        self,
        name: str,
    ) -> None:
        """
        Remove a registered sensor.
        """
        self._sensors.pop(name, None)

    def read(
        self,
        name: str,
    ) -> Any:
        """
        Read data from a sensor.
        """
        if name not in self._sensors:
            raise KeyError(
                f"Sensor '{name}' is not registered."
            )

        return self._sensors[name]()

    def read_all(self) -> Dict[str, Any]:
        """
        Read all registered sensors.
        """
        data = {}

        for name, callback in self._sensors.items():
            try:
                data[name] = callback()
            except Exception as e:
                data[name] = {
                    "error": str(e)
                }

        return data

    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Check whether a sensor exists.
        """
        return name in self._sensors

    def sensors(self) -> List[str]:
        """
        Return registered sensor names.
        """
        return sorted(self._sensors.keys())

    def clear(self) -> None:
        """
        Remove all sensors.
        """
        self._sensors.clear()

    def timestamp(self) -> str:
        """
        Return the current timestamp.
        """
        return datetime.utcnow().isoformat()

    def info(self) -> Dict[str, Any]:
        """
        Return sensor manager information.
        """
        return {
            "module": "SensorPerception",
            "registered_sensors": len(self._sensors),
            "sensors": self.sensors(),
        }

    def __len__(self):
        return len(self._sensors)

    def __contains__(self, name: str):
        return name in self._sensors

    def __repr__(self):
        return (
            f"SensorPerception("
            f"sensors={len(self._sensors)})"
        )