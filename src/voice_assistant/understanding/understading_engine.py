from abc import ABC, abstractmethod

from voice_assistant.entities import Action


class UnderstadingEngine(ABC):
    @abstractmethod
    def extract_action_from_text(self, text: str) -> Action:
        raise NotImplemented()
