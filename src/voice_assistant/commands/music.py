from typing import Dict

from voice_assistant.commands import Command


class MusicCommand(Command):

    def __init__(self, function_name: str, function_parameters: Dict[str, object]):
        super().__init__(function_name, function_parameters)

    def play(self):
        return 'bi bi bi bi bi bi po po bi bi po po bi bi po po'