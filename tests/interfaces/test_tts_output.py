from voice_assistant.interfaces.output import TTSOutput

from tests import BaseTest


class TestTTSOutput(BaseTest):
    def test_tts_output(self):
        output = TTSOutput('pt')
        output.syntethize('oi tudo bem?')
        self.stream_mock.write.assert_called_once()
