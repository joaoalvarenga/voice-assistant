from typing import Optional

from sentence_transformers import SentenceTransformer, util
from voice_assistant.entities import Action
from voice_assistant.understanding import UnderstadingEngine


class IntentEngine(UnderstadingEngine):
    def __init__(self):
        super().__init__()
        self.__model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-mpnet-base-v2',
                                           device='cpu')
        self.__pre_compute_intent_embeddings()
        self.__threshold = 0.6

    def __pre_compute_intent_embeddings(self):
        self.__intent_keys = list(self.actions.keys())
        self.__intent_embeddings = self.__model.encode(self.__intent_keys, convert_to_tensor=True)

    def extract_action_from_text(self, text: str) -> Optional[Action]:
        text_embedding = self.__model.encode(text, convert_to_tensor=True)
        scores = util.pytorch_cos_sim(text_embedding, self.__intent_embeddings)
        pairs = sorted([(self.__intent_keys[i], score) for i, score in enumerate(scores.cpu().numpy()[0])],
                       reverse=True, key=lambda x: x[1])
        best_match = pairs[0]
        if best_match[1] < self.__threshold:
            return None
        return self.actions[best_match[0]]