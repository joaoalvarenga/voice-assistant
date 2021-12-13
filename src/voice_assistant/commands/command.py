from abc import ABC, abstractmethod
from typing import Dict

from voice_assistant.entities import CommandParameters


class Command(ABC):
    @classmethod
    @abstractmethod
    def build_command(cls, parameters: CommandParameters) -> 'Command':
        raise NotImplemented()

    @abstractmethod
    def execute(self):
        raise NotImplemented()