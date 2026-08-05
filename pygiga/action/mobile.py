"""
pygiga.action.mobile
====================

Mobile Action Module

Provides mobile device interaction.

Author: PyGiga
"""

import platform
import subprocess
from typing import List, Dict


class MobileAction:
    """
    Mobile device utilities.
    """

    def __init__(self):
        pass

    # --------------------------------------------------
    # Device Information
    # --------------------------------------------------

    def info(self) -> Dict[str, str]:
        """
        Return host system information.
        """

        return {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
            "processor": platform.processor(),
        }

    # --------------------------------------------------
    # Android (ADB)
    # --------------------------------------------------

    def connected_devices(self) -> List[str]:
        """
        Return connected Android devices using ADB.
        """

        try:

            result = subprocess.run(
                ["adb", "devices"],
                capture_output=True,
                text=True,
                check=True,
            )

            lines = result.stdout.splitlines()[1:]

            devices = []

            for line in lines:

                if "\tdevice" in line:
                    devices.append(line.split("\t")[0])

            return devices

        except Exception:

            return []

    def install_apk(
        self,
        apk_path: str,
    ) -> bool:
        """
        Install an APK.
        """

        try:

            subprocess.run(
                ["adb", "install", apk_path],
                check=True,
            )

            return True

        except Exception:

            return False

    def uninstall_package(
        self,
        package_name: str,
    ) -> bool:
        """
        Uninstall an application.
        """

        try:

            subprocess.run(
                ["adb", "uninstall", package_name],
                check=True,
            )

            return True

        except Exception:

            return False

    def open_application(
        self,
        package_name: str,
    ) -> bool:
        """
        Launch an Android application.
        """

        try:

            subprocess.run(
                [
                    "adb",
                    "shell",
                    "monkey",
                    "-p",
                    package_name,
                    "-c",
                    "android.intent.category.LAUNCHER",
                    "1",
                ],
                check=True,
            )

            return True

        except Exception:

            return False

    def shell(
        self,
        command: str,
    ) -> str:
        """
        Execute an ADB shell command.
        """

        try:

            result = subprocess.run(
                ["adb", "shell"] + command.split(),
                capture_output=True,
                text=True,
                check=True,
            )

            return result.stdout

        except Exception as e:

            return str(e)