# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) > 0 and len(postorder) > 0:
            root_val = postorder[-1]

            root_idx = inorder.index(root_val)
            left_inorder = inorder[0:root_idx]
            right_inorder = inorder[root_idx + 1:]

            left_postorder = []
            right_postorder = []

            i = 0
            while i < len(postorder) and len(left_inorder) > 0:
                val = postorder[i]
                if val in left_inorder:
                    left_postorder = postorder[i:i + len(left_inorder)]
                    i = i + len(left_inorder)
                    break
                else:
                    i += 1

            while i < len(postorder):
                val = postorder[i]
                if val in right_inorder:
                    right_postorder = postorder[i:i + len(right_inorder)]
                    i = i + len(right_inorder)
                else:
                    i += 1

            node = TreeNode(val=root_val)
            node.left = self.buildTree(left_inorder, left_postorder)
            node.right = self.buildTree(right_inorder, right_postorder)
            return node
        else:
            return None


def printTree(node: Optional[TreeNode]):
    if node:
        if node.left:
            printTree(node.left)
        print(node.val)
        if node.right:
            printTree(node.right)


if __name__ == '__main__':
    s = Solution()
    root = s.buildTree([1, 2], [2, 1])
    printTree(root)
