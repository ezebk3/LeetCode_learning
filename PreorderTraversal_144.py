# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution_144:
    def __init__(self):
        self.r_list = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            self.r_list.append(root.val)
            if root.left:
                self.preorderTraversal(root.left)
            if root.right:
                self.preorderTraversal(root.right)

        return self.r_list

    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        r_stack = []
        if root:
            t_stack = [root]

            while len(t_stack) > 0:
                node = t_stack.pop()
                r_stack.append(node.val)
                if node.right:
                    t_stack.append(node.right)
                if node.left:
                    t_stack.append(node.left)

        return r_stack


if __name__ == '__main__':
    root_ = TreeNode(val=1, left=None, right=TreeNode(val=2, left=TreeNode(val=3), right=None))

    s = Solution_144()
    print(s.preorderTraversal2(root_))
