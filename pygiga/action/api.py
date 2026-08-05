"""
pygiga.action.api
=================

API Action Module

Provides an interface for interacting with REST APIs.

Author: PyGiga
"""

from typing import Any, Dict, Optional
import requests


class APIAction:
    """
    Execute HTTP API requests.
    """

    def __init__(self, timeout: int = 30):
        self.timeout = timeout

    def get(
        self,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """
        Perform a GET request.
        """
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=self.timeout,
        )

        return self._format_response(response)

    def post(
        self,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """
        Perform a POST request.
        """
        response = requests.post(
            url,
            data=data,
            json=json,
            headers=headers,
            timeout=self.timeout,
        )

        return self._format_response(response)

    def put(
        self,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """
        Perform a PUT request.
        """
        response = requests.put(
            url,
            data=data,
            json=json,
            headers=headers,
            timeout=self.timeout,
        )

        return self._format_response(response)

    def delete(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """
        Perform a DELETE request.
        """
        response = requests.delete(
            url,
            headers=headers,
            timeout=self.timeout,
        )

        return self._format_response(response)

    def patch(
        self,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """
        Perform a PATCH request.
        """
        response = requests.patch(
            url,
            data=data,
            json=json,
            headers=headers,
            timeout=self.timeout,
        )

        return self._format_response(response)

    def head(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """
        Perform a HEAD request.
        """
        response = requests.head(
            url,
            headers=headers,
            timeout=self.timeout,
        )

        return self._format_response(response)

    def options(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """
        Perform an OPTIONS request.
        """
        response = requests.options(
            url,
            headers=headers,
            timeout=self.timeout,
        )

        return self._format_response(response)

    def _format_response(self, response: requests.Response) -> Dict[str, Any]:
        """
        Convert a requests.Response into a dictionary.
        """
        try:
            body = response.json()
        except Exception:
            body = response.text

        return {
            "status": response.status_code,
            "success": response.ok,
            "headers": dict(response.headers),
            "body": body,
            "url": response.url,
        }