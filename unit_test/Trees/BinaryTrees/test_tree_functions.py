import unittest

from ExecuteCode import execution_helper
from Trees.BinaryTrees.tree_functions import create_tree_from_array, level_order_traversal


class TestTreeFunctions(unittest.TestCase):
    def test_level_order(self):
        in_arr = execution_helper.generate_array(10, -10, 10)
        root = create_tree_from_array(in_arr)
        output = level_order_traversal(root)
        self.assertEqual(in_arr, output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
