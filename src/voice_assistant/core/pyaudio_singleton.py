import pyaudio


class PyAudioSingleton:
    __INSTANCE = None

    def __init__(self):
        self.py_audio = pyaudio.PyAudio()

    @classmethod
    def get_instance(cls):
        if cls.__INSTANCE is None:
            cls.__INSTANCE = PyAudioSingleton()
        return cls.__INSTANCE
