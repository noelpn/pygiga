"""Simulation engine."""

class Simulation:
    """Runs simple world simulations."""

    def __init__(self):
        self.steps = 0

    def step(self):
        self.steps += 1

    def status(self):
        return {'steps': self.steps}
