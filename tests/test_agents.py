from pygiga.agents import AgentCoordinator


def test_agent_coordinator_loads():
    coordinator = AgentCoordinator()
    assert coordinator is not None
    assert hasattr(coordinator, 'run')
