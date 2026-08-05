"""
pygiga.agents.manager
=====================

Agent Manager

Responsible for managing all agents in PyGiga.

Author: PyGiga
"""


class AgentManager:
    """
    Manage registered agents.
    """

    def __init__(self):

        self._agents = {}

    # --------------------------------------------------
    # Register
    # --------------------------------------------------

    def register(self, name: str, agent) -> bool:
        """
        Register an agent.
        """

        self._agents[name] = agent
        return True

    # --------------------------------------------------
    # Unregister
    # --------------------------------------------------

    def unregister(self, name: str) -> bool:
        """
        Remove an agent.
        """

        if name in self._agents:
            del self._agents[name]
            return True

        return False

    # --------------------------------------------------
    # Get Agent
    # --------------------------------------------------

    def get(self, name: str):
        """
        Get an agent by name.
        """

        return self._agents.get(name)

    # --------------------------------------------------
    # Check
    # --------------------------------------------------

    def exists(self, name: str) -> bool:

        return name in self._agents

    # --------------------------------------------------
    # Names
    # --------------------------------------------------

    def names(self):

        return list(self._agents.keys())

    # --------------------------------------------------
    # Count
    # --------------------------------------------------

    def count(self):

        return len(self._agents)

    # --------------------------------------------------
    # All Agents
    # --------------------------------------------------

    def agents(self):

        return self._agents

    # --------------------------------------------------
    # Execute
    # --------------------------------------------------

    def execute(self, name: str, method: str, *args, **kwargs):
        """
        Execute a method on an agent.
        """

        agent = self.get(name)

        if agent is None:
            raise ValueError(
                f"Agent '{name}' not found."
            )

        if not hasattr(agent, method):
            raise AttributeError(
                f"{name} has no method '{method}'."
            )

        function = getattr(agent, method)

        return function(*args, **kwargs)

    # --------------------------------------------------
    # Broadcast
    # --------------------------------------------------

    def broadcast(
        self,
        method: str,
        *args,
        **kwargs,
    ):
        """
        Execute the same method on every agent.
        """

        results = {}

        for name, agent in self._agents.items():

            if hasattr(agent, method):

                try:

                    results[name] = getattr(
                        agent,
                        method
                    )(*args, **kwargs)

                except Exception as e:

                    results[name] = str(e)

        return results

    # --------------------------------------------------
    # Status
    # --------------------------------------------------

    def status(self):

        status = {}

        for name, agent in self._agents.items():

            if hasattr(agent, "info"):

                status[name] = agent.info()

            else:

                status[name] = {
                    "status": "registered"
                }

        return status

    # --------------------------------------------------
    # Clear
    # --------------------------------------------------

    def clear(self):

        self._agents.clear()

    # --------------------------------------------------
    # Information
    # --------------------------------------------------

    def info(self):

        return {
            "registered_agents": self.count(),
            "agents": self.names(),
        }