class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(ino, pre):
    ino_map = {val: idx for idx,val in enumerate(ino)}
    pre_idx = 0

    def helper(left, right):
        nonlocal pre_idx
        if left>right:
            return None
        root_val = pre[pre_idx]
        pre_idx += 1

        root = TreeNode(root_val)
        root.left = helper(left, ino_map[root_val]-1)
        root.right = helper(ino_map[root_val]+1, right)

        return root

    return helper(0, len(ino)-1)