import unittest
from datetime import datetime

from voice_assistant.commands.time import TimeCommand
from voice_assistant.entities import CommandParameters


class TestTimeCommand(unittest.TestCase):

    def test_what_time_is(self):
        parameters = CommandParameters(
            function_name='what_time_is',
            function_args=dict()
        )

        time_command = TimeCommand.build_command(parameters)
        response = time_command.execute()
        self.assertEqual(response, datetime.now().strftime('%H horas e %M minutos'))