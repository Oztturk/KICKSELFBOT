# ☘️ KICK SELF BOT

This project allows you to use your own Kick channel like a bot — send messages, react to followers, and automate simple tasks using your personal account.

---

## 📦 Features

- 🧩 **Customizable commands** — Add your own trigger-based responses.
- 👋 **Follower & unfollow messages** — Automatically send welcome or goodbye messages.
- ⚙️ **Easy setup and use** — Minimal configuration required, just plug in your Kick token.

---

## ⚙️ Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/<your-username>/kick-self-bot.git
    cd kick-self-bot
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

🧪 Configuration

    ```env
        KICK_AUTH_TOKEN=YOUR_KICK_AUTH_TOKEN_HERE
        CHANNEL_NAME=YOUR_CHANNEL_NAME_HERE
    ```
    ❗Never share your auth token publicly. Treat it like a password.


🚀 Usage
    ```bash
    python src/main.py
    or
    python -m src.main
    ```
📁 Project Structure

```
src/
├── API/
│   ├── __init__.py
│   ├── Auth.py
│   └── Message.py
│
├── Classes/
│   ├── __init__.py
│   ├── CommandClass.py
│   └── Ratelimit.py
│
├── Commands/
│   ├── __init__.py
│   └── Ping.py
│
├── config/
│   ├── __init__.py
│   └── Config.py
│
└── Websocket/
    ├── __init__.py
    ├── ws.py
    └── main.py

.env.example
.gitignore
README.md
requirements.txt
```

Explanation:

``API/`` → Handles Kick API communication (auth, messages)
``Classes/`` → Core classes like command handler and rate limiter
``Commands/`` → Your custom bot commands
``config/`` → Environment and configuration management
``Websocket/`` → WebSocket client that connects and listens to events

‼️Notes
    This project is for educational and personal use only.
    Using self bots may violate Kick’s Terms of Service — use responsibly.
