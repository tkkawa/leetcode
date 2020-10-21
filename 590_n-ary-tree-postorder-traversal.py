# v = node num
# time : O(v)
# space : O(v)

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ret = []
        if root is None:
            return None
        def recpost(root):
            if root.children is None:
                return None
            for child in root.children:
                recpost(child)
                ret.append(child.val)
        recpost(root)
        ret.append(root.val)
        return ret
