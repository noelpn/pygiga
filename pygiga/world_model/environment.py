"""World environment."""

class Environment:
    """Represents a simulation environment."""

    def __init__(self):
        self.name = 'default'

    def info(self):
        return {'environment': self.name, 'status': 'initialized'}
