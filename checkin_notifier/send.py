"""Utilities for sending a payload to a generic HTTP webhook."""
import json
import requests

def post_message(url: str, text: str) -> None:
    """POST a JSON payload ``{"text": <text>}`` to *url*.

    Raises ``requests.HTTPError`` on non‑2xx responses.
    """
    headers = {"Content-Type": "application/json"}
    payload = {"text": text}
    response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=10)
    response.raise_for_status()
