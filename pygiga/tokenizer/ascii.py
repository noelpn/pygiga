"""ASCII tokenizer."""

class AsciiTokenizer:
    """Simple ASCII tokenizer.""

    def tokenize(self, text):
        return [c for c in text]

    def detokenize(self, tokens):
        return ''.join(tokens)
