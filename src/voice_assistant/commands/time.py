from typing import Dict

from voice_assistant.commands.command import Command
from datetime import datetime

from voice_assistant.entities import CommandParameters


class TimeCommand(Command):
    def __init__(self, function_name: str, function_parameters: Dict[str, object]):
        self.function_name = function_name
        self.function_parameters = function_parameters

    def what_time_is(self):
        return datetime.now().strftime('%H horas e %M minutos')

    @classmethod
    def build_command(cls, parameters: CommandParameters) -> 'Command':
        if parameters.function_name is None:
            raise Exception("Function name is null")

        if getattr(TimeCommand, parameters.function_name) is None:
            raise Exception(f'Function {parameters.function_name} does not exists on TimeCommand')

        return TimeCommand(parameters.function_name, parameters.function_args)

    def execute(self):
        method = getattr(TimeCommand, self.function_name)
        return method(self, **self.function_parameters)

