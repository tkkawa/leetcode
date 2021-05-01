# n = nodes num
# time = O(n)
# space = O(n)
# done time = 40m


from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        stack = deque([[root, targetSum - root.val]])
        while stack:
            root = stack.pop()
            if not root[0].left and not root[0].right:
                if root[1] == 0:
                    return True
            if root[0].left:
                stack.append([root[0].left, root[1] - root[0].left.val])
            if root[0].right:
                stack.append([root[0].right, root[1] - root[0].right.val])
        return False
