import unittest
import datetime as realdatetime
from unittest import mock

from num2words import num2words
from voice_assistant.commands.time import TimeCommand
from voice_assistant.entities import CommandParameters


class TestTimeCommand(unittest.TestCase):

    @mock.patch('voice_assistant.commands.time.datetime')
    def test_what_time_is(self, mock_datetime):
        mock_datetime.datetime.now.return_value = realdatetime.datetime(1996, 8, 4, 14, 34, 8, 0)
        parameters = CommandParameters(
            function_name='what_time_is',
            function_args=dict()
        )

        time_command = TimeCommand.build_command(parameters)
        response = time_command.execute()

        self.assertEqual(response,
                         'catorze horas e trinta e quatro minutos...')

    @mock.patch('voice_assistant.commands.time.datetime')
    def test_today_is(self, mock_datetime):
        mock_datetime.datetime.now.return_value = realdatetime.datetime(1996, 8, 4, 14, 34, 8, 0)
        parameters = CommandParameters(
            function_name='today_is'
        )

        time_command = TimeCommand.build_command(parameters)
        response = time_command.execute()

        self.assertEqual(response, 'domingo quatro de agosto de mil novecentos e noventa e seis')