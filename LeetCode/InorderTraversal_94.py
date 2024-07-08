# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution_94:
    def __init__(self):
        self.t_stack = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            if root.left:
                self.inorderTraversal(root.left)
            self.t_stack.append(root.val)
            if root.right:
                self.inorderTraversal(root.right)

    def inorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        r_stack = []
        t_stack = []
        if root:
            cur = root
            while cur or t_stack:
                while cur:
                    t_stack.append(cur)
                    cur = cur.left

                cur = t_stack.pop()
                r_stack.append(cur.val)
                cur = cur.right

        return r_stack


if __name__ == '__main__':
    # root_ = TreeNode(val=1, left=None, right=TreeNode(val=2, left=TreeNode(val=3), right=None))
    root_ = TreeNode(val=1, right=None, left=TreeNode(val=2, right=TreeNode(val=3), left=None))

    s = Solution_94()
    print(s.inorderTraversal1(root_))
