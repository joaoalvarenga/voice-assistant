from typing import Dict, Any
from pydantic import BaseModel


class CommandParameters(BaseModel):
    function_name: str
    function_args: Dict[str, Any] = dict()
