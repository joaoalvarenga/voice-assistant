from abc import ABC
import torch
import numpy as np
from voice_assistant.interfaces.speech_recognition import SpeechRecognitionEngine
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor


class Wav2Vec2Engine(SpeechRecognitionEngine):
    def __init__(self, model_name: str, device: str):
        self.device = device
        self.model = Wav2Vec2ForCTC.from_pretrained(model_name).to(device)
        self.processor = Wav2Vec2Processor.from_pretrained(model_name)

    def recognize(self, signal: bytes) -> str:
        signal = np.frombuffer(signal, dtype=np.int16) / 32767
        inputs = self.processor([signal], return_tensors="pt", padding=True, sampling_rate=16_000)
        with torch.no_grad():
            logits = self.model(inputs.input_values.to(self.device),
                                attention_mask=inputs.attention_mask.to("cuda")).logits
            pred_ids = torch.argmax(logits, dim=-1)
            return self.processor.batch_decode(pred_ids)[0].lower()
