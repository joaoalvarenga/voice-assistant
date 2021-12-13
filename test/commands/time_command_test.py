import unittest
from datetime import datetime

from num2words import num2words
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
        hour, minutes = datetime.now().strftime('%H %M').split(' ')

        self.assertEqual(response,
                         f"{num2words(hour, lang='pt-br')} horas e {num2words(minutes, lang='pt-br')} minutos...")