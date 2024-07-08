# Definition for a binary tree node.
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution_102:
    def levelOrder1(self, root: Optional[TreeNode]) -> List[List[int]]:
        r_list = []
        if root:
            t_que = deque([root])
            while t_que:
                level = []
                for _ in range(len(t_que)):

                    cur = t_que.popleft()
                    if cur.left:
                        t_que.append(cur.left)
                    if cur.right:
                        t_que.append(cur.right)

                    level.append(cur.val)

                r_list.append(level)

        return r_list

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        r_list = []
        if root:
            self.levelAdd(root, 0, r_list=r_list)

        return r_list

    def levelAdd(self, node: Optional[TreeNode], level, r_list):
        if node:
            if len(r_list) == level:
                r_list.append([])

            r_list[level].append(node.val)
            if node.left:
                self.levelAdd(node.left, level=level + 1, r_list=r_list)
            if node.right:
                self.levelAdd(node.right, level=level + 1, r_list=r_list)


if __name__ == '__main__':
    root = TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)))

    s = Solution_102()
    print(s.levelOrder1(root))
