# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)
    # v = node.length
    # e = edge.length
    # time : O(v+e)
    # space : O(v)
