import unittest
from unittest.mock import patch, Mock


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.pyaudio_patch = patch('voice_assistant.core.pyaudio_singleton.pyaudio')
        self.mock_pyaudio = self.pyaudio_patch.start()
        self.addCleanup(self.pyaudio_patch.stop)
        stream_mock = Mock()
        stream_mock.write.return_value = None

        pyaudio_mock = Mock()
        pyaudio_mock.open.return_value = stream_mock

        self.mock_pyaudio.PyAudio.return_value = pyaudio_mock
        self.stream_mock = stream_mock
