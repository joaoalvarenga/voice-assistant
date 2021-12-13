import json

import gdown
import pyaudio
import torch
import numpy as np
from TTS.config import load_config
from TTS.tts.models import setup_model
from TTS.tts.utils.synthesis import synthesis
from TTS.utils.audio import AudioProcessor

from voice_assistant.interfaces.output import Output


def download_files():
    gdown.cached_download('https://drive.google.com/uc?id=1-PfXD66l1ZpsZmJiC-vhL055CDSugLyP',
                   'config.json',
                   quiet=False)
    gdown.cached_download('https://drive.google.com/uc?id=1_Vb2_XHqcC0OcvRF82F883MTxfTRmerg',
                   'language_ids.json', quiet=False)
    gdown.cached_download('https://drive.google.com/uc?id=1SZ9GE0CBM-xGstiXH2-O2QWdmSXsBKdC',
                   'speakers.json', quiet=False)
    gdown.cached_download('https://drive.google.com/uc?id=1sgEjHt0lbPSEw9-FSbC_mBoOPwNi87YR',
                   'best_model.pth.tar', quiet=False)


class TTSOutput(Output):
    def __init__(self, language: str):
        super().__init__(language)
        download_files()
        self.config = load_config('config.json')
        self.audio_processor = AudioProcessor(**self.config.audio)
        speaker_embedding = None

        self.config.model_args['d_vector_file'] = 'speakers.json'
        self.config.model_args['use_speaker_encoder_as_loss'] = False

        self.model = setup_model(self.config)
        self.model.language_manager.set_language_ids_from_file('language_ids.json')
        # print(model.language_manager.num_languages, model.embedded_language_dim)
        # print(model.emb_l)
        cp = torch.load('best_model.pth.tar', map_location=torch.device('cpu'))
        # remove speaker encoder
        model_weights = cp['model'].copy()
        for key in list(model_weights.keys()):
            if "speaker_encoder" in key:
                del model_weights[key]

        self.model.load_state_dict(model_weights)

        self.model.eval()

        with open('speakers.json') as f:
            self.speakers = json.load(f)

        # synthesize voice
        use_griffin_lim = False
        self.language_id = 2
        self.pyaudio = pyaudio.PyAudio()
        self.stream = self.pyaudio.open(format=pyaudio.paInt16, channels=1,
                                   rate=self.audio_processor.sample_rate, output=True)

    def syntethize(self, text: str):
        self.model.length_scale = 1  # scaler for the duration predictor. The larger it is, the slower the speech.
        self.model.inference_noise_scale = 0.3  # defines the noise variance applied to the random z vector at inference.
        self.model.inference_noise_scale_dp = 0.3  # defines the noise variance applied to the duration predictor z vector at inference.
        output = synthesis(
                    self.model,
                    text,
                    self.config,
                    "cuda" in str(next(self.model.parameters()).device),
                    self.audio_processor,
                    speaker_id=None,
                    d_vector=self.speakers['common_voice_pt_19288283.wav']['embedding'],
                    style_wav=None,
                    language_id=self.language_id,
                    enable_eos_bos_chars=self.config.enable_eos_bos_chars,
                    use_griffin_lim=True,
                    do_trim_silence=False,
                )
        self.audio_processor.save_wav(output['wav'], 'output.wav')
        wav = output['wav']
        wav = wav * (32767 / max(0.01, np.max(np.abs(wav))))
        self.stream.write(wav.astype(np.int16).tobytes())

    def render(self, text: str):
        self.syntethize(text)

    def render_not_recognized(self):
        self.syntethize(self._not_recognized[self.language])
