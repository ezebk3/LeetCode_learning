# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.arr = []

    def inorder(self, root: Optional[TreeNode]):

        if root:
            if root.left:
                self.getMinimumDifference(root.left)
            self.arr.append(root.val)
            if root.right:
                self.getMinimumDifference(root.right)

    def findMin(self):

        min_d = float("inf")
        for i in range(len(self.arr)):
            if i < len(self.arr) - 1:
                df = abs(self.arr[i] - self.arr[i + 1])
                if df < min_d:
                    min_d = df

        return min_d

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.inorder(root)
        return self.findMin()
