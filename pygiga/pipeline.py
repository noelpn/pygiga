"""Pipeline orchestration."""

class Pipeline:
    """Defines a reusable AGI pipeline."""

    def __init__(self, agi=None):
        self.agi = agi

    def run(self, prompt):
        if self.agi is None:
            raise RuntimeError('AGI instance is required')
        return self.agi.ask(prompt)
