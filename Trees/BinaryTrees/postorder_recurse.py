# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        def post(root, ans):
            if root == None:
                return
            post(root.left, ans)
            post(root.right, ans)
            ans.append(root.val)

        ans = []
        post(root, ans)
        return ans
