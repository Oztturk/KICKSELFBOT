import os
import importlib

def load_commands():
    commands_dir = os.path.dirname(__file__)
    for filename in os.listdir(commands_dir):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = f"src.Commands.{filename[:-3]}"
            importlib.import_module(module_name)
            print(f"Loaded command module: {module_name}")
