# Definition for a binary tree node.
from typing import List, Optional
from gen_Tree import MyTree
import copy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.path_r = []

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.inorder(root, [])
        # print(self.path_r)
        return self.path_r

    def inorder(self, node: Optional[TreeNode], path_list):
        if node:
            path_t = path_list.copy()
            path_t.append(node.val)
            if not node.right and not node.left:
                self.path_r.append("->".join(str(num) for num in path_t))
            else:
                if node.left:
                    self.inorder(node.left, path_t)
                if node.right:
                    self.inorder(node.right, path_t)


def demo_t():
    a = [1, 2, 3]
    b = a.copy()
    del a[0]
    print(b)


if __name__ == '__main__':
    root = MyTree([1, 2, 3, None, 5]).root
    s = Solution()
    s.binaryTreePaths(root)
    # demo_t()
