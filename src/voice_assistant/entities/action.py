from typing import Callable, Dict

from dataclasses import dataclass


@dataclass
class Action:
    name: str
    command: Callable
    parameters: Dict[str, object]