"""
pygiga.agents.action_agent
==========================

Action Agent

Responsible for executing plans using the ActionExecutor.

Author: PyGiga
"""

from pygiga.action import ActionExecutor


class ActionAgent:
    """
    Executes plans produced by the planner.
    """

    def __init__(self):

        self.executor = ActionExecutor()

    # --------------------------------------------------
    # Execute Plan
    # --------------------------------------------------

    def execute(self, plan):
        """
        Execute a plan.

        Parameters
        ----------
        plan : dict

        Returns
        -------
        dict
        """

        return self.executor.execute(plan)

    # --------------------------------------------------
    # Terminal
    # --------------------------------------------------

    def terminal(self, command):

        return self.executor.terminal_command(command)

    # --------------------------------------------------
    # Browser
    # --------------------------------------------------

    def browser(self, url):

        return self.executor.open_browser(url)

    # --------------------------------------------------
    # File System
    # --------------------------------------------------

    def read_file(self, path):

        return self.executor.read_file(path)

    def write_file(
        self,
        path,
        content,
    ):

        return self.executor.write_file(
            path,
            content,
        )

    # --------------------------------------------------
    # API
    # --------------------------------------------------

    def api_get(self, url):

        return self.executor.get(url)

    def api_post(
        self,
        url,
        data=None,
        json=None,
    ):

        return self.executor.post(
            url,
            data=data,
            json=json,
        )

    # --------------------------------------------------
    # Desktop
    # --------------------------------------------------

    def application(self, app):

        return self.executor.open_application(app)

    def open_file(self, path):

        return self.executor.open_file(path)

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

        return self.executor.send_email(
            to=to,
            subject=subject,
            body=body,
            attachments=attachments,
        )

    # --------------------------------------------------
    # Status
    # --------------------------------------------------

    def info(self):

        return {
            "agent": "ActionAgent",
            "executor": "ActionExecutor",
            "status": "ready",
        }