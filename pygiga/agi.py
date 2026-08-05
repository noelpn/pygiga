"""AGI core orchestrator."""

from .agents import AgentCoordinator

class AGI:
    """Top-level AGI assistant."""

    def __init__(self):
        self.coordinator = AgentCoordinator()

    def ask(self, prompt):
        return self.coordinator.run(prompt)

    def info(self):
        return {'assistant': 'PyGiga', 'status': 'ready'}
