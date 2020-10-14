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
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        stack = deque([root])
        ret = 0
        if root is None:
            return 0
        while stack:
            root = stack.popleft()
            if root.val % 2 == 0:
                if root.left:
                    ret += root.left.left.val if root.left.left else 0
                    ret += root.left.right.val if root.left.right else 0
                if root.right:
                    ret += root.right.left.val if root.right.left else 0
                    ret += root.right.right.val if root.right.right else 0
            if root.right is None and root.left is None:
                continue
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return ret
