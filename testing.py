import unittest
from main import write_to_file, counting_discount


class MyTestCase(unittest.TestCase):
    def test_counting_discount_1(self):
        write_to_file([50, 20, 30, 17, 100], 10)
        self.assertEqual(counting_discount(), 207.00)

    def test_counting_discount_2(self):
        write_to_file([1, 2, 3, 4, 5, 6, 7], 100)
        self.assertEqual(counting_discount(), 15.00)

    def test_counting_discount_3(self):
        write_to_file([1, 1, 1], 33)
        self.assertEqual(counting_discount(), 2.67)


if __name__ == '__main__':
    unittest.main()
