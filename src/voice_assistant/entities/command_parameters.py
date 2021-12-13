from typing import Dict

from dataclasses import dataclass


@dataclass
class CommandParameters:
    function_name: str
    function_args: Dict[str, object]
