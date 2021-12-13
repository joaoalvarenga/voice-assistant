from voice_assistant.interfaces.audio import AudioStream
from voice_assistant.interfaces.audio.microphone_stream import MicrophoneStream
from voice_assistant.interfaces.speech_recognition import Wav2Vec2Engine, SpeechRecognitionEngine
from voice_assistant.understanding import UnderstadingEngine, SentenceMatchEngine


def main(audio_stream: AudioStream,
         asr_engine: SpeechRecognitionEngine,
         understanding_engine: UnderstadingEngine):
    buffer = b''
    while True:
        try:
            frame = audio_stream.get_frames()
            if len(frame) > 0:
                buffer += frame
                continue

            if len(buffer) == 0:
                buffer = b''
                continue

            text = asr_engine.recognize(buffer)
            print(text)

        except KeyboardInterrupt:
            audio_stream.stop()
            break


if __name__ == '__main__':
    print('Initializing Voice Assistant')
    asr_engine = Wav2Vec2Engine('jonatasgrosman/wav2vec2-large-xlsr-53-portuguese', 'cpu')
    understading_engine = SentenceMatchEngine()
    microphone_stream = MicrophoneStream()

    main(microphone_stream, asr_engine, understading_engine)
