"""
pygiga.action.email
===================

Email Action Module

Provides email sending functionality.

Author: PyGiga
"""

import smtplib
from email.message import EmailMessage
from pathlib import Path
from typing import List, Optional


class EmailAction:
    """
    Send emails using SMTP.
    """

    def __init__(
        self,
        smtp_server: str,
        smtp_port: int,
        username: str,
        password: str,
        use_tls: bool = True,
    ):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
        self.use_tls = use_tls

    def send(
        self,
        to: str,
        subject: str,
        body: str,
        attachments: Optional[List[str]] = None,
        html: bool = False,
    ) -> bool:
        """
        Send an email.
        """

        message = EmailMessage()

        message["From"] = self.username
        message["To"] = to
        message["Subject"] = subject

        if html:
            message.add_alternative(body, subtype="html")
        else:
            message.set_content(body)

        if attachments:

            for file in attachments:

                path = Path(file)

                if not path.exists():
                    continue

                with open(path, "rb") as f:

                    data = f.read()

                message.add_attachment(
                    data,
                    maintype="application",
                    subtype="octet-stream",
                    filename=path.name,
                )

        try:

            server = smtplib.SMTP(
                self.smtp_server,
                self.smtp_port,
            )

            if self.use_tls:
                server.starttls()

            server.login(
                self.username,
                self.password,
            )

            server.send_message(message)

            server.quit()

            return True

        except Exception as e:

            print("Email Error:", e)

            return False