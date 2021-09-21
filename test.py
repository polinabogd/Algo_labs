import unittest
from merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_asc_sorting(self):
        self.assertEqual(merge_sort([1, 3, -2, 0, 9], "asc"), [-2, 0, 1, 3, 9])

    def test_desc_sorting(self):
        self.assertEqual(merge_sort([1, 3, -2, 0, 9], "desc"), [9, 3, 1, 0, -2])

    def test_asc_sorting_sorted_by_asc(self):
        self.assertEqual(merge_sort([1, 3, -2, 0, 9], "asc"), [-2, 0, 1, 3, 9])

    def test_asc_sorting_sorted_by_desc(self):
        self.assertEqual(merge_sort([9, 3, 1, 0, -2], "asc"), [-2, 0, 1, 3, 9])

    def test_desc_sorting_sorted_by_asc(self):
        self.assertEqual(merge_sort([1, 3, -2, 0, 9], "desc"), [9, 3, 1, 0, -2])

    def test_desc_sorting_sorted_by_desc(self):
        self.assertEqual(merge_sort([9, 3, 1, 0, -2], "desc"), [9, 3, 1, 0, -2])


if __name__ == '__main__':
    unittest.main()
