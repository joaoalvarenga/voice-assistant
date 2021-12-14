from typing import Dict

from num2words import num2words
from voice_assistant.commands.command import Command
import datetime
from babel.dates import format_datetime

import locale

class TimeCommand(Command):
    def __init__(self, function_name: str, function_parameters: Dict[str, object]):
        super().__init__(function_name, function_parameters)

    def what_time_is(self):
        hour, minutes = datetime.datetime.now().strftime('%H %M').split(' ')
        return f"{num2words(hour, lang='pt-br')} horas e {num2words(minutes, lang='pt-br')} minutos..."

    def today_is(self):
        weekday, day, month, year = format_datetime(datetime.datetime.now(), 'EEEE d MMMM y', locale='pt_BR').split(' ')
        return f"{weekday} {num2words(day, lang='pt-br')} de {month} de {num2words(year, lang='pt-br')}"

    def tomorrow(self):
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        weekday, day, month, year = format_datetime(tomorrow, 'EEEE d MMMM y', locale='pt_BR')
        return f"{weekday} {num2words(day, lang='pt-br')} de {month} de {num2words(year, lang='pt-br')}"


