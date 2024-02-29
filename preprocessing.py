import re


def preprocess(input_string: str) -> str:
    pattern = r'\[(\w+)\s*:\s*([^\]]+)\]'
    cleaned_string = re.sub(pattern, r'\2', input_string)
    return cleaned_string
