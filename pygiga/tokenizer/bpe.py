"""Byte Pair Encoding tokenizer stub."""

class BPETokenizer:
    """Minimal BPE-style tokenizer stub.""

    def tokenize(self, text):
        return text.split()

    def detokenize(self, tokens):
        return ' '.join(tokens)
