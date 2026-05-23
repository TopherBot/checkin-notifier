# checkin-notifier

A tiny Python tool that sends a configurable message to a Slack webhook (or any HTTP endpoint). Perfect for crontab or personal health‑check scripts.

## Features
- One‑file implementation (plus a tiny package)
- Zero runtime dependencies except `requests`
- Configurable via environment variables
- GitHub Actions CI with linting, tests and Bandit security scan

## Usage
```sh
export WEBHOOK_URL="https://hooks.slack.com/services/…"
export MESSAGE="🟢 I'm alive!"
python -m checkin_notifier
```

## Development
```sh
pip install -r requirements.txt
pytest
flake8 *.py
bandit -r .
```

## License
MIT © 2024 TopherBot
