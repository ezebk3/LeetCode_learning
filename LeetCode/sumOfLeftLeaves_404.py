# Definition for a binary tree node.
from typing import Optional
from gen_Tree import MyTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.left_total = 0

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.count_left(root, False)
        return self.left_total
        pass

    def count_left(self, node, is_left):
        if node:
            if is_left and not node.left and not node.right:
                self.left_total += node.val

            if node.left:
                self.count_left(node.left, True)

            if node.right:
                self.count_left(node.right, False)


if __name__ == '__main__':
    root = MyTree([3, 9, 20, None, None, 15, 7]).root
    s = Solution()
    print(s.sumOfLeftLeaves(root))

