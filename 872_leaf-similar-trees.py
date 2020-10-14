# v = node num
# time : O(v)
# space : O(v)
# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def makeLeaflist(self, root):
        ret = []
        stack =deque([root])
        if root is None:
            return 0
        while stack:
            root = stack.pop()
            if root.right is None and root.left is None:
                ret.append(root.val)
                continue
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return ret
    
    
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        ret1 = self.makeLeaflist(root1)
        ret2 = self.makeLeaflist(root2)
        print(ret1)
        print(ret2)
        return ret1 == ret2
