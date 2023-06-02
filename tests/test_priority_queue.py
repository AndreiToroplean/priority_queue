import pytest

from priority_queue.priority_queue import PriorityQueue


class TestPriorityQueue:
    def test_highest_priority_first_out(self):
        queue = PriorityQueue()
        queue.put({'command': 'command_a', 'priority': 1})
        queue.put({'command': 'command_b', 'priority': 2})

        assert queue.get() == {'command': 'command_b', 'priority': 2}

    def test_first_in_first_out(self):
        queue = PriorityQueue()
        queue.put({'command': 'command_a', 'priority': 1})
        queue.put({'command': 'command_b', 'priority': 1})

        assert queue.get() == {'command': 'command_a', 'priority': 1}

    def test_get_from_empty_queue(self):
        queue = PriorityQueue()
        assert queue.get() is None

    @pytest.mark.parametrize('invalid_value', [
        None,
        1,
        'string',
        [],
        {},
        {'command': 'command_a'},
        {'priority': 1},
        {'command': 'command_a', 'priority': 1, 'extra': 'extra'},
        {'command': None, 'priority': 1},
        {'command': 'command_a', 'priority': 'string'},
        {'command': 'command_a', 'priority': 15},
    ])
    def test_put_invalid_value(self, invalid_value):
        queue = PriorityQueue()
        with pytest.raises(ValueError):
            queue.put(invalid_value)
