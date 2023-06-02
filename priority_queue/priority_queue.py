class PriorityQueue:
    """A priority queue that can store dicts with a "command" and "priority" keys.

    If two items have the same priority, the first item put in the queue will be the first item out
    of the queue.
    """
    def __init__(self):
        self._queue = []

    def put(self, value: dict):
        """Put the given value in the queue.

        :param value: A dict with a "command" and "priority" keys. The "command" must be a string
            and the "priority" must be an integer between 0 and 10 included.
        :raises ValueError: If the value is not valid.
        """
        if not isinstance(value, dict):
            raise ValueError('Invalid value: not a dict')

        if value.keys() != {'command', 'priority'}:
            raise ValueError('Invalid value: did not contain command and priority keys')

        if not isinstance(value['command'], str):
            raise ValueError('Invalid value: command is not a string')

        if not isinstance(value['priority'], int):
            raise ValueError('Invalid value: priority is not an integer')

        if not 0 <= value['priority'] <= 10:
            raise ValueError('Invalid value: priority is not between 0 and 10')

        self._queue.append(value)

    def get(self) -> dict | None:
        """Get the value with the highest priority.

        If two items have the same priority, the first item put in the queue will be the first item
        out of the queue.

        :return: The first value with the highest priority or None if the queue is empty.
        """
        if not self._queue:
            return None

        # The max function will return the first maximal item encountered, ensuring we respect
        # the first in first out specification. Cf:
        # https://docs.python.org/3/library/functions.html#max
        highest_priority = max(self._queue, key=lambda item: item['priority'])
        self._queue.remove(highest_priority)
        return highest_priority
