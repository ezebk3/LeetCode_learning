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

    def postorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            if root.left:
                self.postorderTraversal(root.left)
            if root.right:
                self.postorderTraversal(root.right)
            self.r_list.append(root.val)

        return self.r_list

    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        r_stack = []
        if root:
            t_stack = [root]

            while len(t_stack) > 0:
                node = t_stack.pop()
                r_stack.append(node.val)
                if node.left:
                    t_stack.append(node.left)
                if node.right:
                    t_stack.append(node.right)

        return r_stack[::-1]

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        r_stack = []
        if root:
            t_stack = [root]
            while t_stack:
                node = t_stack.pop()
                if node:
                    t_stack.append(node)
                    t_stack.append(None)
                    if node.right:
                        t_stack.append(node.right)
                    if node.left:
                        t_stack.append(node.left)
                else:
                    cur = t_stack.pop()
                    r_stack.append(cur.val)

        return r_stack


if __name__ == '__main__':
    root_ = TreeNode(val=1, left=None, right=TreeNode(val=2, left=TreeNode(val=3), right=None))

    s = Solution_144()
    print(s.postorderTraversal(root_))
