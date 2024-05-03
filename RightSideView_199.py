# Definition for a binary tree node.
from typing import Optional, List

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution_199:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        r_list = []
        if root:
            t_que = deque([root])
            while t_que:
                level_len = len(t_que)
                level_view = None
                for idx in range(level_len):

                    cur = t_que.popleft()
                    if cur.left:
                        t_que.append(cur.left)
                    if cur.right:
                        t_que.append(cur.right)

                    if idx == level_len - 1:
                        level_view = cur.val

                r_list.append(level_view)

        return r_list


if __name__ == '__main__':
    root = TreeNode(val=1, left=TreeNode(val=2, right=TreeNode(val=5, right=TreeNode(val=6))),
                    right=TreeNode(val=3, right=TreeNode(val=4)))
    s = Solution_199()
    print(s.rightSideView(root))
