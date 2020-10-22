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
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        stack = deque([root])
        while stack:
            root = stack.popleft()
            if root.left is None and root.right is None:
                continue
            if root.left:
                stack.append(root.left)
                if root.val != root.left.val:
                    return False
            if root.right:
                stack.append(root.right)
                if root.val != root.right.val:
                    return False
        return True
