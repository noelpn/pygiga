# pygiga/safety/permissions.py

from enum import Enum
from dataclasses import dataclass


class Permission(Enum):
    READ_FILE = "read_file"
    WRITE_FILE = "write_file"
    DELETE_FILE = "delete_file"

    INTERNET_ACCESS = "internet_access"

    EXECUTE_CODE = "execute_code"
    INSTALL_PACKAGE = "install_package"

    ACCESS_CAMERA = "access_camera"
    ACCESS_MICROPHONE = "access_microphone"

    SEND_EMAIL = "send_email"

    DATABASE_READ = "database_read"
    DATABASE_WRITE = "database_write"

    SYSTEM_COMMAND = "system_command"


@dataclass
class PermissionResult:
    allowed: bool
    reason: str = ""


class PermissionManager:
    def __init__(self):
        self.permissions = {
            Permission.READ_FILE: True,
            Permission.WRITE_FILE: True,
            Permission.DELETE_FILE: False,

            Permission.INTERNET_ACCESS: True,

            Permission.EXECUTE_CODE: False,
            Permission.INSTALL_PACKAGE: False,

            Permission.ACCESS_CAMERA: False,
            Permission.ACCESS_MICROPHONE: False,

            Permission.SEND_EMAIL: False,

            Permission.DATABASE_READ: True,
            Permission.DATABASE_WRITE: True,

            Permission.SYSTEM_COMMAND: False,
        }

    def allow(self, permission: Permission):
        self.permissions[permission] = True

    def deny(self, permission: Permission):
        self.permissions[permission] = False

    def check(self, permission: Permission) -> PermissionResult:
        if self.permissions.get(permission, False):
            return PermissionResult(True)

        return PermissionResult(
            False,
            f"{permission.value} permission denied."
        )