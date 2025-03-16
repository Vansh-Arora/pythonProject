import unittest
from parameterized import parameterized
from Sorting_techniques.bubble_sort import bubble_sort
from Sorting_techniques.insertion_sort import insertion_sort
from Sorting_techniques.merge_sort import merge_sort
from Sorting_techniques.quick_sort import quick_sort
from Sorting_techniques.selection_sort import selection_sort


class TestSort(unittest.TestCase):

    @parameterized.expand([
        ([5, 3, 8, 1, 2], [1, 2, 3, 5, 8]),
        ([], []),
        ([7], [7]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([4, 2, 2, 4, 3], [2, 2, 3, 4, 4]),
        ([-3, -1, -7, -2, -5], [-7, -5, -3, -2, -1]),  # Negative numbers
        ([1000, 500, 100, 50, 10, 5, 1], [1, 5, 10, 50, 100, 500, 1000]),  # Large numbers
        ([1] * 1000, [1] * 1000),  # Large array with identical elements
        ([i for i in range(1000, 0, -1)], [i for i in range(1, 1001)]),  # Large reversed array
        ([0, -1, 1, -2, 2, -3, 3], [-3, -2, -1, 0, 1, 2, 3]),  # Mixed positive and negative
    ])
    def test_bubble_sort_cases(self, arr, expected):
        bubble_sort(arr)
        self.assertEqual(arr, expected)

    @parameterized.expand([
        ([5, 3, 8, 1, 2], [1, 2, 3, 5, 8]),
        ([], []),
        ([7], [7]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([4, 2, 2, 4, 3], [2, 2, 3, 4, 4]),
        ([-3, -1, -7, -2, -5], [-7, -5, -3, -2, -1]),  # Negative numbers
        ([1000, 500, 100, 50, 10, 5, 1], [1, 5, 10, 50, 100, 500, 1000]),  # Large numbers
        ([1] * 1000, [1] * 1000),  # Large array with identical elements
        ([i for i in range(1000, 0, -1)], [i for i in range(1, 1001)]),  # Large reversed array
        ([0, -1, 1, -2, 2, -3, 3], [-3, -2, -1, 0, 1, 2, 3]),  # Mixed positive and negative
    ])
    def test_quick_sort_cases(self, arr, expected):
        quick_sort(arr,0 ,len(arr)-1)
        self.assertEqual(arr, expected)

    @parameterized.expand([
        ([5, 3, 8, 1, 2], [1, 2, 3, 5, 8]),
        ([], []),
        ([7], [7]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([4, 2, 2, 4, 3], [2, 2, 3, 4, 4]),
        ([-3, -1, -7, -2, -5], [-7, -5, -3, -2, -1]),  # Negative numbers
        ([1000, 500, 100, 50, 10, 5, 1], [1, 5, 10, 50, 100, 500, 1000]),  # Large numbers
        ([1] * 1000, [1] * 1000),  # Large array with identical elements
        ([i for i in range(1000, 0, -1)], [i for i in range(1, 1001)]),  # Large reversed array
        ([0, -1, 1, -2, 2, -3, 3], [-3, -2, -1, 0, 1, 2, 3]),  # Mixed positive and negative
    ])
    def test_selection_sort_cases(self, arr, expected):
        selection_sort(arr)
        self.assertEqual(arr, expected)

    @parameterized.expand([
        ([5, 3, 8, 1, 2], [1, 2, 3, 5, 8]),
        ([], []),
        ([7], [7]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([4, 2, 2, 4, 3], [2, 2, 3, 4, 4]),
        ([-3, -1, -7, -2, -5], [-7, -5, -3, -2, -1]),  # Negative numbers
        ([1000, 500, 100, 50, 10, 5, 1], [1, 5, 10, 50, 100, 500, 1000]),  # Large numbers
        ([1] * 1000, [1] * 1000),  # Large array with identical elements
        ([i for i in range(1000, 0, -1)], [i for i in range(1, 1001)]),  # Large reversed array
        ([0, -1, 1, -2, 2, -3, 3], [-3, -2, -1, 0, 1, 2, 3]),  # Mixed positive and negative
    ])
    def test_insertion_sort_cases(self, arr, expected):
        insertion_sort(arr)
        self.assertEqual(arr, expected)
    @parameterized.expand([
        ([5, 3, 8, 1, 2], [1, 2, 3, 5, 8]),
        ([], []),
        ([7], [7]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([4, 2, 2, 4, 3], [2, 2, 3, 4, 4]),
        ([-3, -1, -7, -2, -5], [-7, -5, -3, -2, -1]),  # Negative numbers
        ([1000, 500, 100, 50, 10, 5, 1], [1, 5, 10, 50, 100, 500, 1000]),  # Large numbers
        ([1] * 1000, [1] * 1000),  # Large array with identical elements
        ([i for i in range(1000, 0, -1)], [i for i in range(1, 1001)]),  # Large reversed array
        ([0, -1, 1, -2, 2, -3, 3], [-3, -2, -1, 0, 1, 2, 3]),  # Mixed positive and negative
    ])
    def test_merge_sort_cases(self, arr, expected):
        merge_sort(arr,0 ,len(arr)-1)
        self.assertEqual(arr, expected)

if __name__ == '__main__':
    unittest.main()
