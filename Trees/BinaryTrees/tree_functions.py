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
        level_size = len(que)
        level = []
        for i in range(level_size):
            curr = que.pop(0)
            level.append(curr.val)
            if curr.left is not None:
                que.append(curr.left)
            if curr.right is not None:
                que.append(curr.right)
        result.append(level)
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


def in_order(root):
    if not root:
        return []
    res = []
    stack = []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        res.append(current.val)
        current = current.right
    return res

def post_order_2_stack(root):
    if root == None:
        return []
    st1 = [root]
    st2 = []
    while st1:
        curr = st1.pop()
        st2.append(curr.val)
        if curr.left:
            st1.append(curr.left)
        if curr.right:
            st1.append(curr.right)
    st2.reverse()
    return st2

def post_order_1_stack(root):
    if root == None:
        return
    st = []
    result = []
    last_visited = None
    curr = root
    while st or curr:
        if curr:
            st.append(curr)
            curr = curr.left
        else:
            top = st[-1]
            if top.right and last_visited != top.right:
                curr = top.right
            else:
                result.append(top)
                last_visited = st.pop()
    return result