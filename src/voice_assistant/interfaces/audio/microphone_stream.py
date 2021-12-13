from typing import Optional

import pyaudio
import webrtcvad
from voice_assistant.interfaces.audio import AudioStream


def get_input_device_id(device_name, microphones):
    for device in microphones:
        if device_name in device[1]:
            return device[0]


def list_microphones(pyaudio_instance):
    info = pyaudio_instance.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')

    result = []
    for i in range(0, numdevices):
        if (pyaudio_instance.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            name = pyaudio_instance.get_device_info_by_host_api_device_index(
                0, i).get('name')
            result += [[i, name]]
    return result


class MicrophoneStream(AudioStream):

    def __init__(self,
                 device_name: str = 'default',
                 vad_mode: int = 1,
                 format: int = pyaudio.paInt16,
                 channels: int = 1,
                 sample_rate: int = 16_000,
                 frame_duration: int = 30,
                 ):
        self.vad = webrtcvad.Vad()
        self.vad.set_mode(vad_mode)

        self.audio = pyaudio.PyAudio()
        self.chunk = int(sample_rate * frame_duration / 1000)

        microphones = list_microphones(self.audio)
        selected_input_device_id = get_input_device_id(device_name, microphones)

        self.stream = self.audio.open(input_device_index=selected_input_device_id,
                                      format=format,
                                      channels=channels,
                                      rate=sample_rate,
                                      input=True,
                                      frames_per_buffer=self.chunk)
        self.sample_rate = sample_rate

    def get_frames(self) -> bytes:
        frame = self.stream.read(self.chunk)
        is_speech = self.vad.is_speech(frame, self.sample_rate)
        if is_speech:
            return frame
        return b''

    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
