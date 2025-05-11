from ExecuteCode import execution_helper
from Trees.BinaryTrees.boundary_order_traversal import boundary_traversal
from Trees.BinaryTrees.lca import lca
from Trees.BinaryTrees.root_to_node_path import getPath
from Trees.BinaryTrees.tree_functions import create_tree_from_array, level_order_traversal, pre_order_traversal, \
    pre_post_in_single_stack, in_order, post_order_1_stack
from Trees.BinaryTrees.Node import Node

# Create
print("Binary Tree")
in_arr = execution_helper.generate_array(5, 0, 10)
print("Input Array", in_arr)
print()

print("Tree Node")
root = create_tree_from_array(in_arr)
print(root.val)
print(root.left.val)
print(root.right.val)
print("Tree Created")
print()

# Level Order Traversal
print("Level Order Traversal")
lot = level_order_traversal(root)
print(lot)
print()

# Pre Order Traversal
print("Pre Order Traversal")
pot = pre_order_traversal(root)
print(pot)
print()

# In Order Traversal
print("In Order Traversal")
iot = in_order(root)
print(iot)
print()


# Post Order Traversal
print("Post Order Traversal")
pot = post_order_1_stack(root)
print(pot)
print()

# All traversals
print("All Traversal")
pre_ord, inorder, post = pre_post_in_single_stack(root)
print("Pre: ", pre_ord)
print("In", inorder)
print("Pot", post)
print()


# Boundary traversal
print("Boundary Traversal")
bot = boundary_traversal(root)
print("Boundary: ", bot)
print()


# Root to node
print("Root to node path")
key = 2
ans = []
path = getPath(root,key,ans)
print(ans)
print()

# LCA
print("LCA")
in_arr = [4,7,6,1,2]
root = create_tree_from_array(in_arr)
print(level_order_traversal(root))
n1 = Node(6)
n2 = Node(2)
ans = lca(root, n1, n2)
print(ans.val)