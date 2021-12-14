import unittest
from datetime import datetime, date

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

    def test_today_is(self):
        parameters = CommandParameters(
            function_name='today_is'
        )

        time_command = TimeCommand.build_command(parameters)
        response = time_command.execute()
        weekday, day, month, year = date.today().strftime("%A %-d %B %Y").split(' ')

        self.assertEqual(response, f"{weekday} {num2words(day, lang='pt-br')} de {month} de {num2words(year, lang='pt-br')}")