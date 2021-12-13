import unittest

from voice_assistant.interfaces.output import TTSOutput


class TestTTSOutput(unittest.TestCase):
    def test_tts_output(self):
        output = TTSOutput('pt')
        output.syntethize('oi tudo bem?')
