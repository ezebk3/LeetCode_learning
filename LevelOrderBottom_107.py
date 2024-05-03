# Definition for a binary tree node.
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution_107:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        r_list = []
        if root:
            m_que = deque([root])
            while m_que:
                level = []
                for _ in range(len(m_que)):
                    cur = m_que.popleft()
                    level.append(cur.val)
                    if cur.left:
                        m_que.append(cur.left)
                    if cur.right:
                        m_que.append(cur.right)
                r_list.append(level)

        return r_list[::-1]


if __name__ == '__main__':
    s = Solution_107()
    root = TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)))
    print(s.levelOrderBottom(root))
