from typing import Callable, Dict

from dataclasses import dataclass
from voice_assistant.entities import CommandParameters


@dataclass
class Action:
    name: str
    command: Callable
    parameters: CommandParameters