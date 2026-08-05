"""Runtime environment for PyGiga."""

from .agi import AGI
from .config import Config

class Runtime:
    """Application runtime wrapper."""

    def __init__(self, config=None):
        self.config = config or Config.load()
        self.agi = AGI()
        self.running = False

    def start(self):
        self.running = True
        print('Runtime started with config:', self.config.settings)

    def stop(self):
        self.running = False
        print('Runtime stopped.')
