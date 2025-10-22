from typing import Callable, List, Dict, Optional
from ..API import send
from .Ratelimit import Ratelimit


class Command:
    _commands: Dict[str, "Command"] = {}

    def __init__(self, name: str, aliases: List[str], callback: Callable, reply: bool, cooldown: float):
        self.name = name
        self.aliases = aliases
        self.callback = callback
        self.reply = reply
        self.ratelimit = Ratelimit(cooldown)

    @classmethod
    def new(cls, data: Dict):
        name = data.get("CommandName")
        aliases = data.get("Aliasses", [])
        callback = data.get("Callback")
        cooldown = data.get("cooldown", 5.0)

        reply = data.get("reply", False)

        if not name or not callable(callback):
            raise ValueError("CommandName veya Callback eksik veya geçersiz.")

        cmd = cls(name, aliases, callback, reply, cooldown)

        cls._commands[name] = cmd
        for alias in aliases:
            cls._commands[alias] = cmd

        return cmd

    @classmethod
    def get(cls, name: str) -> Optional["Command"]:
        return cls._commands.get(name)

    @classmethod
    def run(cls, message_content: str, sender: str, *args, **kwargs):
        command_name = message_content.split()[0]
        cmd = cls.get(command_name)
        if not cmd:
            return False

        if not cmd.ratelimit.check(slug=sender, command=command_name):
            print(cmd.ratelimit.remaining(slug=sender, command=command_name))
            return True
        response_message = cmd.callback(message=message_content, sender=sender, *args, **kwargs)

        if response_message:
            if cmd.reply and sender:
                send(f"@{sender} {response_message}")
            else:
                send(response_message)

        return True
