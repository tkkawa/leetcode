# v = node num
# time : O(v^2)
# space : O(v)
# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        ele = []
        if root is None:
            return False
        stack = deque([root])
        while stack:
            root = stack.popleft()
            if root is None:
                continue
            ele.append(root.val)
            stack.append(root.left)
            stack.append(root.right)
        for i in range(len(ele)):
            element = ele[i]
            ele.pop(i)
            if k - element in ele:
                return True
            ele.insert(i, element)
        return False
