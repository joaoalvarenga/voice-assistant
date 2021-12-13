from abc import ABC, abstractmethod
from typing import Dict

from voice_assistant.entities import CommandParameters


class Command(ABC):
    def __init__(self, function_name: str, function_parameters: Dict[str, object]):
        self.function_name = function_name
        self.function_parameters = function_parameters

    @classmethod
    def build_command(cls, parameters: CommandParameters) -> 'Command':
        if parameters.function_name is None:
            raise Exception("Function name is null")

        if getattr(cls, parameters.function_name) is None:
            raise Exception(f'Function {parameters.function_name} does not exists on {cls}')

        return cls(parameters.function_name, parameters.function_args)

    def execute(self):
        method = getattr(type(self), self.function_name)
        return method(self, **self.function_parameters)