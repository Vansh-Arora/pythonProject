def is_leaf(root):
    if not root.left and not root.right:
        return True
    return False

def add_left(root):
    left_nodes = []
    curr = root.left
    while curr and not is_leaf(curr):
        left_nodes.append(curr.val)
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right
    return left_nodes

def add_right(root):
    right_nodes = []
    curr = root.right
    while curr and not is_leaf(curr):
        right_nodes.append(curr.val)
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left
    return right_nodes

def add_leaves(root, leaves):
    if not root: return
    if is_leaf(root):
        leaves.append(root.val)
    add_leaves(root.left, leaves)
    add_leaves(root.right, leaves)


def boundary_traversal(root):
    if root == None:
        return
    left = add_left(root)
    right = add_right((root))
    leavess = []
    add_leaves(root, leavess)
    return [root.val] + left + leavess + right[::-1]