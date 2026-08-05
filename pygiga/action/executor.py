"""
pygiga.action.executor
======================

Central Action Executor

Routes actions to the correct module.

Author: PyGiga
"""

from .terminal import TerminalAction
from .browser import BrowserAction
from .filesystem import FileSystemAction
from .api import APIAction
from .database import DatabaseAction
from .email import EmailAction
from .desktop import DesktopAction
from .mobile import MobileAction
from .robotics import RoboticsAction


class ActionExecutor:
    """
    Central action execution engine.
    """

    def __init__(self):

        self.terminal = TerminalAction()
        self.browser = BrowserAction()
        self.filesystem = FileSystemAction()
        self.api = APIAction()
        self.database = DatabaseAction()
        self.desktop = DesktopAction()
        self.mobile = MobileAction()
        self.robotics = RoboticsAction()

        # Email requires SMTP credentials.
        # Initialize it later using configure_email().
        self.email = None

    def configure_email(
        self,
        smtp_server,
        smtp_port,
        username,
        password,
        use_tls=True,
    ):
        """
        Configure email support.
        """

        self.email = EmailAction(
            smtp_server=smtp_server,
            smtp_port=smtp_port,
            username=username,
            password=password,
            use_tls=use_tls,
        )

    # --------------------------------------------------
    # Terminal
    # --------------------------------------------------

    def terminal_command(self, command):

        return self.terminal.run(command)

    # --------------------------------------------------
    # Browser
    # --------------------------------------------------

    def open_browser(self, url):

        return self.browser.open(url)

    def search(self, query):

        return self.browser.search_google(query)

    # --------------------------------------------------
    # File System
    # --------------------------------------------------

    def read_file(self, path):

        return self.filesystem.read(path)

    def write_file(self, path, content):

        return self.filesystem.write(path, content)

    # --------------------------------------------------
    # API
    # --------------------------------------------------

    def get(self, url):

        return self.api.get(url)

    def post(self, url, data=None, json=None):

        return self.api.post(
            url,
            data=data,
            json=json,
        )

    # --------------------------------------------------
    # Database
    # --------------------------------------------------

    def execute_sql(self, query):

        return self.database.execute(query)

    def fetch_all(self, query):

        return self.database.fetch_all(query)

    # --------------------------------------------------
    # Desktop
    # --------------------------------------------------

    def open_application(self, app):

        return self.desktop.open_application(app)

    def open_file(self, path):

        return self.desktop.open_file(path)

    # --------------------------------------------------
    # Email
    # --------------------------------------------------

    def send_email(
        self,
        to,
        subject,
        body,
        attachments=None,
    ):

        if self.email is None:
            raise RuntimeError(
                "EmailAction is not configured."
            )

        return self.email.send(
            to=to,
            subject=subject,
            body=body,
            attachments=attachments,
        )

    # --------------------------------------------------
    # Mobile
    # --------------------------------------------------

    def mobile_action(self):

        return self.mobile.info()

    # --------------------------------------------------
    # Robotics
    # --------------------------------------------------

    def robotics_action(self):

        return self.robotics.info()

    # --------------------------------------------------
    # Generic Execute
    # --------------------------------------------------

    def execute(self, plan):
        """
        Execute a generic plan.

        For now this simply returns the plan.
        Later versions can automatically dispatch
        to the correct action module.
        """

        return {
            "status": "success",
            "plan": plan,
        }