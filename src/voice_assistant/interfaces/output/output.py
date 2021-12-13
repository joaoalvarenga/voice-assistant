from abc import ABC, abstractmethod


class Output(ABC):
    def __init__(self, language: str):
        self.language = language
        self._not_recognized = {
            'pt': 'Desculpe, não entendi',
            'en': 'Sorry, didn\'t get it'
        }

    @abstractmethod
    def render(self, text: str):
        raise NotImplemented()

    @abstractmethod
    def render_not_recognized(self):
        raise NotImplemented()