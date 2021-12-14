from typing import Dict

from num2words import num2words
from voice_assistant.commands.command import Command
from datetime import datetime, date, timedelta
from babel.dates import format_date
from voice_assistant.entities import CommandParameters

import locale

class TimeCommand(Command):
    def __init__(self, function_name: str, function_parameters: Dict[str, object]):
        super().__init__(function_name, function_parameters)

    def what_time_is(self):
        hour, minutes = datetime.now().strftime('%H %M').split(' ')
        return f"{num2words(hour, lang='pt-br')} horas e {num2words(minutes, lang='pt-br')} minutos..."

    def today_is(self):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        weekday, day, month, year = date.today().strftime("%A %-d %B %Y").split(' ')
        return f"{weekday} {num2words(day, lang='pt-br')} de {month} de {num2words(year, lang='pt-br')}"

    def tomorrow(self):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        tomorrow = date.today() + timedelta(days=1)
        weekday, day, month, year = tomorrow.strftime("%A %-d %B %Y").split(' ')
        return f"{weekday} {num2words(day, lang='pt-br')} de {month} de {num2words(year, lang='pt-br')}"


