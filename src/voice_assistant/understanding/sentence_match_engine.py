from typing import Optional

from voice_assistant.commands.time import TimeCommand
from voice_assistant.entities import Action, CommandParameters
from voice_assistant.understanding import UnderstadingEngine


class SentenceMatchEngine(UnderstadingEngine):
    def __init__(self):
        super().__init__()

    def extract_action_from_text(self, text: str) -> Optional[Action]:
        for sentence in self.actions:
            if text.lower().find(sentence) > -1:
                return self.actions[sentence]
        return None
