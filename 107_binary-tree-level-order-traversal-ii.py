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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        stack = deque([root])
        ret = []
        while stack:
            ret_mid = []
            for i in range(len(stack)):
                root = stack.popleft()
                if root is None:
                    continue
                ret_mid.append(root.val)
                stack.append(root.left)
                stack.append(root.right)
            if len(ret_mid) == 0:
                continue
            ret.append(ret_mid)
        ret.reverse()
        return ret
