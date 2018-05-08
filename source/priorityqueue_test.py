#!python

from priorityqueue import PriorityQueue
import unittest

class PriorityQueueTest(unittest.TestCase):

    def test_init(self):
        p = PriorityQueue()
        assert p.length() == 0
        assert p.is_empty() is True
        assert p.front() is None

    def test_is_empty(self):
        p = PriorityQueue()
        assert p.is_empty() is True
        p.enqueue('A', 1)
        assert p.is_empty() is False
        p.enqueue('B', 1)
        assert p.is_empty() is False
        p.dequeue()
        assert p.is_empty() is False
        p.dequeue()
        assert p.is_empty() is True

    def test_length(self):
        p = PriorityQueue()
        p.enqueue('A', 1)
        assert p.length() == 1
        p.enqueue('B', 1)
        assert p.length() == 2
        p.enqueue('C', 2)
        assert p.length() == 3
        p.dequeue()
        assert p.length() == 2
        p.dequeue()
        assert p.length() == 1
        p.dequeue()
        assert p.length() == 0

    def test_enqueue(self):
        p = PriorityQueue()
        assert p.heap.items == []
        p.enqueue('A', 2)
        assert p.heap.items == [(2, 'A')]
        p.enqueue('B', 2)
        assert p.heap.items == [(2, 'A'), (2, 'B')]
        p.enqueue('C', 1)
        assert p.heap.items == [(1, 'C'), (2, 'B'), (2, 'A')]
        p.enqueue('D', 1)
        assert p.heap.items == [(1, 'C'), (1, 'D'), (2, 'A'), (2, 'B')]
        p.enqueue('E', 3)
        assert p.heap.items == [(1, 'C'), (1, 'D'), (2, 'A'), (2, 'B'), (3, 'E')]
        p.enqueue('F', 2)
        assert p.heap.items == [(1, 'C'), (1, 'D'), (2, 'A'), (2, 'B'), (3, 'E'), (2, 'F')]

    def test_front(self):
        p = PriorityQueue()
        assert p.front() is None
        p.enqueue('A', 2)
        assert p.front() == 'A'
        p.enqueue('B', 2)
        assert p.front() == 'A'
        p.enqueue('C', 1)
        assert p.front() == 'C'
        p.dequeue()
        assert p.front() == 'A'
        p.dequeue()
        assert p.front() == 'B'

    def test_dequeue(self):
        p = PriorityQueue()
        assert p.heap.items == []
        p.enqueue('A', 2)
        assert p.heap.items == [(2, 'A')]
        p.enqueue('B', 2)
        assert p.heap.items == [(2, 'A'), (2, 'B')]
        p.enqueue('C', 1)
        assert p.heap.items == [(1, 'C'), (2, 'B'), (2, 'A')]
        p.enqueue('D', 1)
        assert p.heap.items == [(1, 'C'), (1, 'D'), (2, 'A'), (2, 'B')]
        p.enqueue('E', 3)
        assert p.heap.items == [(1, 'C'), (1, 'D'), (2, 'A'), (2, 'B'), (3, 'E')]
        p.enqueue('F', 2)
        assert p.heap.items == [(1, 'C'), (1, 'D'), (2, 'A'), (2, 'B'), (3, 'E'), (2, 'F')]
        assert p.dequeue() == 'C'
        assert p.heap.items == [(1, 'D'), (2, 'B'), (2, 'A'), (2, 'F'), (3, 'E')]
        assert p.dequeue() == 'D'
        assert p.heap.items == [(2, 'A'), (2, 'B'), (3, 'E'), (2, 'F')]
        assert p.dequeue() == 'A'
        assert p.heap.items == [(2, 'B'), (2, 'F'), (3, 'E')]
        assert p.dequeue() == 'B'
        assert p.heap.items == [(2, 'F'), (3, 'E')]
        assert p.dequeue() == 'F'
        assert p.heap.items == [(3, 'E')]
        assert p.dequeue() == 'E'
        assert p.heap.items == []
        with self.assertRaises(ValueError):
            p.dequeue()

    def test_push_pop(self):
        p = PriorityQueue()
        assert p.heap.items == []
        p.enqueue('A', 2)
        assert p.heap.items == [(2, 'A')]
        p.enqueue('B', 2)
        assert p.heap.items == [(2, 'A'), (2, 'B')]
        p.enqueue('C', 1)
        assert p.heap.items == [(1, 'C'), (2, 'B'), (2, 'A')]
        p.enqueue('D', 1)
        assert p.heap.items == [(1, 'C'), (1, 'D'), (2, 'A'), (2, 'B')]
        p.enqueue('E', 3)
        assert p.heap.items == [(1, 'C'), (1, 'D'), (2, 'A'), (2, 'B'), (3, 'E')]
        p.enqueue('F', 2)
        assert p.heap.items == [(1, 'C'), (1, 'D'), (2, 'A'), (2, 'B'), (3, 'E'), (2, 'F')]
        assert p.push_pop('G', 1) == 'C'
        assert p.heap.items == [(1, 'D'), (1, 'G'), (2, 'A'), (2, 'B'), (3, 'E'), (2, 'F')]
        assert p.push_pop('H', 2) == 'D'
        assert p.heap.items == [(1, 'G'), (2, 'B'), (2, 'A'), (2, 'H'), (3, 'E'), (2, 'F')]
        assert p.push_pop('I', 3) == 'G'
        assert p.heap.items == [(2, 'A'), (2, 'B'), (2, 'F'), (2, 'H'), (3, 'E'), (3, 'I')]
        assert p.push_pop('J', 4) == 'A'
        assert p.heap.items == [(2, 'B'), (2, 'H'), (2, 'F'), (4, 'J'), (3, 'E'), (3, 'I')]
        assert p.push_pop('K', 1) == 'B'
        assert p.heap.items == [(1, 'K'), (2, 'H'), (2, 'F'), (4, 'J'), (3, 'E'), (3, 'I')]
        assert p.push_pop('L', 3) == 'K'
        assert p.heap.items == [(2, 'F'), (2, 'H'), (3, 'I'), (4, 'J'), (3, 'E'), (3, 'L')]
        # with self.assertRaises(ValueError):
        #     p.dequeue()
