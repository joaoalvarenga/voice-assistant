from abc import ABC, abstractmethod
from typing import Optional


class AudioStream(ABC):
    @abstractmethod
    def get_frames(self) -> bytes:
        raise NotImplemented()

    @abstractmethod
    def stop(self):
        raise NotImplemented()