# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        def ino(root, ans):
            if root == None:
                return
            ino(root.left,ans)
            ans.append(root.val)
            ino(root.right, ans)
        ans = []
        ino(root, ans)
        return ans