# n = node num
# time = O(n)
# space = O(n)
# done time = 15m


from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1

        min_val = root.val
        second_min_val = float('inf')
        stack = deque([root])
        while stack:
            root = stack.pop()
            if min_val < root.val < second_min_val:
                second_min_val = root.val
            if not root.left and not root.right:
                continue
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)

        if second_min_val == float('inf'):
            return -1

        return second_min_val
