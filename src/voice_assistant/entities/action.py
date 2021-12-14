from typing import Callable

from pydantic import BaseModel
from voice_assistant.entities import CommandParameters


class Action(BaseModel):
    name: str
    command: Callable
    parameters: CommandParameters
