import unittest
from datetime import datetime

from num2words import num2words
from voice_assistant.understanding import IntentEngine


class TestIntentEngine(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.intent_engine = IntentEngine()

    def test_what_time_is_variation(self):
        action_response = self.intent_engine.extract_action_from_text('horas')
        self.assertIsNotNone(action_response)

        command_response = action_response.command(action_response.parameters).execute()
        self.assertIsNotNone(command_response)

        hour, minutes = datetime.now().strftime('%H %M').split(' ')

        self.assertEqual(command_response,
                         f"{num2words(hour, lang='pt-br')} horas e {num2words(minutes, lang='pt-br')} minutos...")

    def test_what_time_is(self):
        action_response = self.intent_engine.extract_action_from_text('me diz a hora')
        self.assertIsNotNone(action_response)

        command_response = action_response.command(action_response.parameters).execute()
        self.assertIsNotNone(command_response)

        hour, minutes = datetime.now().strftime('%H %M').split(' ')

        self.assertEqual(command_response,
                         f"{num2words(hour, lang='pt-br')} horas e {num2words(minutes, lang='pt-br')} minutos...")