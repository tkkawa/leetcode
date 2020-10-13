# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        stack = deque([[root, 1]])
        if root is None:
            return 0
        maxDepth = 1
        ret = []
        res = 0
        while stack:
            root, depth = stack.popleft()
            if root.left is None and root.right is None:
                ret.append([root.val, depth])
                maxDepth = max(maxDepth, depth)
                continue
            depth += 1
            if root.left:
                stack.append([root.left, depth])
            if root.right:
                stack.append([root.right, depth])
        for i in range(len(ret)):
            if ret[i][1] == maxDepth:
                res += ret[i][0]
        return res
    # v = node.length
    # n = leaf.length
    # time : O(v)
    # space : O(n)
