from voice_assistant.interfaces.output import Output


class TextOutput(Output):
    def __init__(self, language: str):
        super().__init__(language)

    def render_not_recognized(self):
        print(self._not_recognized[self.language])

    def render(self, text: str):
        print(text)
