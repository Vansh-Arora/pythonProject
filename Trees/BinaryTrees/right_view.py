from collections import deque
def right_view(root):
    que = deque([root])
    result = []
    while que:
        level_length = len(que)
        for i in range(level_length):
            node = que.popleft()
            if i == level_length-1:
                result.append(node.data)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
    return result

