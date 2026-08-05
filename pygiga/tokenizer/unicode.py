"""Unicode tokenizer."""

class UnicodeTokenizer:
    """Simple unicode-aware tokenizer.""

    def tokenize(self, text):
        return text.split()

    def detokenize(self, tokens):
        return ' '.join(tokens)
