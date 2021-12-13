from typing import Dict

from num2words import num2words
from voice_assistant.commands.command import Command
from datetime import datetime

from voice_assistant.entities import CommandParameters


class TimeCommand(Command):
    def __init__(self, function_name: str, function_parameters: Dict[str, object]):
        super().__init__(function_name, function_parameters)

    def what_time_is(self):
        hour, minutes = datetime.now().strftime('%H %M').split(' ')
        return f"{num2words(hour, lang='pt-br')} horas e {num2words(minutes, lang='pt-br')} minutos..."

