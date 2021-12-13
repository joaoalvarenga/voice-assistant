from abc import abstractmethod, ABC
import numpy as np


class SpeechRecognitionEngine(ABC):
    @abstractmethod
    def recognize(self, signal: bytes) -> str:
        raise NotImplemented()
