# PyGiga API

This document describes the main public interfaces available in PyGiga.

- `pygiga.AGI` – top-level assistant entrypoint.
- `pygiga.agents.AgentCoordinator` – controls the perception-memory-reasoning-planning-action pipeline.
- `pygiga.action.ActionExecutor` – executes actions such as shell commands, browser navigation, filesystem operations, and API calls.
- `pygiga.communication.ConversationManager` – stores and manages chat history.
- `pygiga.knowledge.DocumentManager` – stores and retrieves documents.
- `pygiga.memory.MemoryManager` – exposes short-term, long-term, episodic, working, and semantic memory.
