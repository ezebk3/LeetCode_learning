from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution_111:
    def __init__(self):
        self.min_depth = 10 ** 6

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            self.in_order(root, 1)
        else:
            return 0
        return self.min_depth

    def in_order(self, node: Optional[TreeNode], level):

        if not node.left and not node.right:
            if self.min_depth > level:
                self.min_depth = level

        if node.left:
            self.in_order(node.left, level + 1)

        if node.right:
            self.in_order(node.right, level + 1)

        return self.min_depth


if __name__ == '__main__':
    pass