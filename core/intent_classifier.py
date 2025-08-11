from sentence_transformers import SentenceTransformer, util
import torch


class IntentClassifier:
    def __init__(self, intent_examples: dict[str, list[str]], model_name: str = "all-MiniLM-L6-v2", threshold: float = 0.45):
        self.model = SentenceTransformer(model_name)
        self.intent_examples = intent_examples
        self.threshold = threshold
        self.index = []  # list of (intent_label, example_embedding)

        self._build_index()

    def _build_index(self):
        for label, examples in self.intent_examples.items():
            embeddings = self.model.encode(examples, convert_to_tensor=True)
            for emb in embeddings:
                self.index.append((label, emb))

    def predict(self, user_input: str):
        input_emb = self.model.encode(user_input, convert_to_tensor=True)
        best_score = -1
        best_label = None

        for label, emb in self.index:
            score = util.cos_sim(input_emb, emb).item()
            if score > best_score:
                best_score = score
                best_label = label

        if best_score >= self.threshold:
            return best_label, best_score
        return None, best_score  # Rejection path
