# Definition for a binary tree node.
from typing import Optional
from tools.build_tree import MyTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_min(self, val, root: Optional[TreeNode]) -> bool:
        if root:
            if root.val <= val:
                return False
            else:
                return self.is_min(val, root.left) and self.is_min(val, root.right)
        else:
            return True

    def is_max(self, val, root: Optional[TreeNode]) -> bool:
        if root:
            if root.val >= val:
                return False
            else:
                return self.is_max(val, root.left) and self.is_max(val, root.right)
        else:
            return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root:
            if self.is_max(root.val, root.left) and self.is_min(root.val, root.right):
                return self.isValidBST(root.left) and self.isValidBST(root.right)
            else:
                return False
        else:
            return True


if __name__ == '__main__':
    tree = MyTree([5, 1, 4, None, None, 3, 6])
    s = Solution()
    print(s.isValidBST(tree.root))
