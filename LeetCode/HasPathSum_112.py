# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.targetSum = None
        self.is_Find = False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.targetSum = targetSum
        self.findSum(root, 0)
        return self.is_Find

    def findSum(self, node: Optional[TreeNode], now_total):
        if node:
            if not node.left and not node.right:
                if self.targetSum == (now_total + node.val):
                    self.is_Find = True
                    return
            if node.left:
                self.findSum(node.left, now_total + node.val)

            if node.right:
                self.findSum(node.right, now_total + node.val)
