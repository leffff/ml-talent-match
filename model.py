from typing import List, Dict

from transformers import pipeline


class NERModel:
    def __init__(self, model_folder: str):
        self.model = pipeline("ner", model=model_folder, aggregation_strategy="simple")

    def __call__(self, text: str) -> List[Dict]:
        return self.model(text)
