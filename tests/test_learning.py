from pygiga.learning.feedback import FeedbackManager


def test_feedback_manager():
    manager = FeedbackManager()
    result = manager.add('Great job')
    assert result['status'] == 'added'
    assert manager.list() == ['Great job']
