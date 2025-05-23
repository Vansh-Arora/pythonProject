# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        def pre(root, ans):
            if root == None:
                return
            ans.append(root.val)
            pre(root.left, ans)
            pre(root.right, ans)

        ans = []
        pre(root, ans)
        return ans
