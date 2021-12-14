import unittest
from datetime import datetime

from num2words import num2words
from voice_assistant.commands import TimeCommand
from voice_assistant.entities import CommandParameters
from voice_assistant.understanding import IntentEngine

from tests import BaseTest


class TestIntentEngine(BaseTest):

    @classmethod
    def setUpClass(cls):
        cls.intent_engine = IntentEngine()

    def test_what_time_is_variation(self):
        action_response = self.intent_engine.extract_action_from_text('horas')
        self.assertIsNotNone(action_response)

        command_response = action_response.command(action_response.parameters).execute()
        self.assertIsNotNone(command_response)

        self.assertEqual(command_response,
                         TimeCommand.build_command(CommandParameters(function_name='what_time_is')).execute())

    def test_what_time_is(self):
        action_response = self.intent_engine.extract_action_from_text('me diz a hora')
        self.assertIsNotNone(action_response)

        command_response = action_response.command(action_response.parameters).execute()
        self.assertIsNotNone(command_response)

        self.assertEqual(command_response,
                         TimeCommand.build_command(CommandParameters(function_name='what_time_is')).execute())