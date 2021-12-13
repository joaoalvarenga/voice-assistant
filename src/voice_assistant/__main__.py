import time

from halo import Halo
from voice_assistant.core import PyAudioSingleton
from voice_assistant.interfaces.audio import AudioStream
from voice_assistant.interfaces.audio.microphone_stream import MicrophoneStream
from voice_assistant.interfaces.output import Output, TTSOutput
from voice_assistant.interfaces.speech_recognition import Wav2Vec2Engine, SpeechRecognitionEngine
from voice_assistant.understanding import UnderstadingEngine, IntentEngine


def main(audio_stream: AudioStream,
         asr_engine: SpeechRecognitionEngine,
         understanding_engine: UnderstadingEngine,
         output: Output):
    buffer = b''
    spinner = Halo(text='Me pergunte as horas, ou peça pra tocar música...', spinner='dots')
    while True:
        try:
            spinner.start()
            frame = audio_stream.get_frames()
            if len(frame) > 0:
                buffer += frame
                continue

            if len(buffer) == 0:
                buffer = b''
                continue
            text = asr_engine.recognize(buffer)
            buffer = b''
            if len(text) == 0:
                continue
            spinner.stop()
            print(text)
            action_response = understanding_engine.extract_action_from_text(text)
            if action_response is None:
                output.render_not_recognized()
                time.sleep(1)
                continue
            command_response = action_response.command(action_response.parameters).execute()
            output.render(command_response)


        except KeyboardInterrupt:
            audio_stream.stop()
            output.stop()
            PyAudioSingleton.get_instance().py_audio.terminate()
            break


if __name__ == '__main__':
    print('Initializing Voice Assistant')
    asr_engine = Wav2Vec2Engine('jonatasgrosman/wav2vec2-large-xlsr-53-portuguese', 'cpu')
    understading_engine = IntentEngine()
    microphone_stream = MicrophoneStream()
    output = TTSOutput('pt')

    main(microphone_stream, asr_engine, understading_engine, output)
