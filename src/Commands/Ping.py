from ..Classes import Command


def run(sender: str, message: str):
    return "PONG!"



commandData = {
        "CommandName": "!ping",
        "Aliasses": ["!p", "!pg"],
        "Callback": run,
        "reply": True,
        "cooldown": 120
    }

Command.new((commandData))
