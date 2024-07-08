# Definition for a binary tree node.
from typing import Optional

from gen_Tree import MyTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution_110:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root:
            lh = self.getHeight(root.left)
            if lh == -1: return False
            rh = self.getHeight(root.right)
            if rh == -1: return False

            return abs(lh - rh) < 2

        else:
            return True

    def getHeight(self, node: Optional[TreeNode]):
        if not node:
            return 0

        lh = self.getHeight(node.left)
        if lh == -1: return -1

        rh = self.getHeight(node.right)
        if rh == -1: return -1

        return -1 if abs(lh - rh) > 1 else 1 + max(rh, lh)


if __name__ == '__main__':
    # root = MyTree([1, None, 2, None, 3]).root
    root = TreeNode(val=1, left=None, right=TreeNode(val=2, right=TreeNode(3)))
    s = Solution_110()
    print(s.isBalanced(root))
