"""Entry point for the check‑in notifier.

Runs when the module is executed as a script.
"""
import os
import sys
from . import send

def _get_env(name: str, default: str | None = None) -> str:
    value = os.getenv(name, default)
    if value is None:
        print(f"Error: environment variable {name} is not set", file=sys.stderr)
        sys.exit(1)
    return value

def main() -> None:
    webhook = _get_env("WEBHOOK_URL")
    message = _get_env("MESSAGE", "✅ Check‑in from checkin‑notifier")
    try:
        send.post_message(webhook, message)
        print("Message sent successfully")
    except Exception as exc:
        print(f"Failed to send message: {exc}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
