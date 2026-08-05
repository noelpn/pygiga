from pygiga.memory.memory_manager import MemoryManager


def test_memory_manager():
    memory = MemoryManager()
    assert memory.recall_short() == []
    memory.remember_short('note')
    assert memory.recall_short() == ['note']
