from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        vals = []

        def dsf(node):
            if node:
                vals.append(node.val)
                dsf(node.left)
                dsf(node.right)

        dsf(root)

        return len(set(vals)) == 1
