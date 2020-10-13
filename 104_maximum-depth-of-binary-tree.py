class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = self.maxDepth(root.left) + 1
        depth = max(depth, self.maxDepth(root.right) + 1)
        return depth
