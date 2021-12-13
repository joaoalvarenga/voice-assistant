from voice_assistant.commands.time import TimeCommand
from voice_assistant.entities import Action, CommandParameters
from voice_assistant.understanding import UnderstadingEngine


class SentenceMatchEngine(UnderstadingEngine):
    def __init__(self):
        self.sentences = {
            'que horas são': Action(
                name='what time is',
                command=TimeCommand.build_command,
                parameters={
                    'parameters': CommandParameters(
                        function_args=dict(),
                        function_name='what_time_is'
                    )
                }
            )
        }

    def extract_action_from_text(self, text: str) -> Action:
        return self.sentences.get(text)
