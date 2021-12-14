from abc import ABC, abstractmethod
from typing import Optional

from voice_assistant.commands import TimeCommand, MusicCommand
from voice_assistant.entities import Action, CommandParameters


class UnderstadingEngine(ABC):
    def __init__(self):
        self.actions = {
            'que horas são': Action(
                name='what time is',
                command=TimeCommand.build_command,
                parameters=CommandParameters(
                    function_args=dict(),
                    function_name='what_time_is'
                )
            ),
            'que dia é hoje': Action(
                name='today is',
                command=TimeCommand.build_command,
                parameters=CommandParameters(
                    function_name='today_is'
                )
            ),
            'amanhã será': Action(
                name='tomorrow',
                command=TimeCommand.build_command,
                parameters=CommandParameters(
                    function_name='tomorrow'
                )
            ),
            'tocar música': Action(
                name='play',
                command=MusicCommand.build_command,
                parameters=CommandParameters(
                    function_args=dict(),
                    function_name='play'
                )
            ),
            'ligar para': None
        }

    @abstractmethod
    def extract_action_from_text(self, text: str) -> Optional[Action]:
        raise NotImplemented()
