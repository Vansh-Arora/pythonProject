from ExecuteCode import execution_helper
from Trees.BinaryTrees.tree_functions import create_tree_from_array, level_order_traversal, pre_order_traversal

# Create
print("Binary Tree")
in_arr = execution_helper.generate_array(5, 0, 10)
print("Input Array", in_arr)

root = create_tree_from_array(in_arr)
print(root.val)
print(root.left.val)
print(root.right.val)
print("Tree Created")

# Level Order Traversal
print("Level Order Traversal")
lot = level_order_traversal(root)
print(lot)

# Pre Order Traversal
print("Pre Order Traversal")
pot = pre_order_traversal(root)
print(pot)