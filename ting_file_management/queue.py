from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._queue = list()

    def __len__(self):
        return len(self._queue)

    def is_empty(self):
        return self._queue == []

    def enqueue(self, value):
        self._queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self._queue.pop(0)

    def search(self, index):
        if index in range(len(self._queue)):
            return self._queue[index]
        raise IndexError("Índice Inválido ou Inexistente")
