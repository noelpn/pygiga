"""Base tokenizer."""

from .ascii import AsciiTokenizer

class Tokenizer:
    """General tokenizer wrapper.""

    def __init__(self):
        self.inner = AsciiTokenizer()

    def tokenize(self, text):
        return self.inner.tokenize(text)

    def detokenize(self, tokens):
        return self.inner.detokenize(tokens)
