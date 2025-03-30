from Trees.BinaryTrees.Node import Node


def create_tree_from_array(arr):
    if not arr:
        return None

    root = Node(arr[0])
    que = [root]
    i = 1
    n = len(arr)
    while i < n:
        current = que.pop(0)
        if i < n:
            current.left = Node(arr[i])
            que.append(current.left)
        i += 1
        if i < n:
            current.right = Node(arr[i])
            que.append(current.right)
        i += 1

    return root


def level_order_traversal(root):
    if not root:
        return []
    que = [root]
    result = []
    while len(que) != 0:
        curr = que.pop(0)
        result.append(curr.val)
        if curr.left is not None:
            que.append(curr.left)
        if curr.right is not None:
            que.append(curr.right)
    return result

def pre_order_traversal(root):
    if not root:
        return
    stck = [root]
    result = []
    while stck:
        curr = stck.pop()
        print(curr.val)
        result.append(curr.val)
        if curr.right is not None:
            stck.append(curr.right)
        if curr.left is not None:
            stck.append(curr.left)
    return result

root = create_tree_from_array([0])
root.left = Node(0)
if root.left:
    print(root)
    print(root.val)