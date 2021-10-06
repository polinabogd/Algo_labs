import unittest
from main import Deque


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.deq = Deque()
        self.deq.insert_front(12)
        self.deq.insert_front(10)
        self.deq.insert_rear(11)
        self.deq.insert_rear(5)

    def test_insert_and_get_front(self):
        self.assertEqual(self.deq.get_front(), 10)

    def test_insert_and_get_rear(self):
        self.assertEqual(self.deq.get_rear(), 5)

    def test_delete_front(self):
        self.assertEqual(self.deq.delete_front(), (4, 3, 12))

    def test_delete_rear(self):
        self.assertEqual(self.deq.delete_rear(), (4, 3, 11))

    def test_getting_lengths(self):
        self.assertEqual(self.deq.deque_length(), 4)

    def test_is_empty(self):
        self.assertEqual(self.deq.is_empty(), False)


if __name__ == '__main__':
    unittest.main()
