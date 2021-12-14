import unittest
from datetime import datetime

from voice_assistant.commands import TimeCommand
from voice_assistant.entities import CommandParameters
from voice_assistant.understanding import SentenceMatchEngine

from tests import BaseTest


class TestSentenceMatchEngine(BaseTest):
    def test_what_time_is(self):
        sentence_match_engine = SentenceMatchEngine()
        action_response = sentence_match_engine.extract_action_from_text('ok google que horas são')
        self.assertIsNotNone(action_response)

        command_response = action_response.command(action_response.parameters).execute()
        self.assertIsNotNone(command_response)
        self.assertEqual(command_response, TimeCommand.build_command(
            CommandParameters(function_name='what_time_is')).execute())