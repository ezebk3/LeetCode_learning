# Definition for a binary tree node.
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution_104:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        r_list = []
        if root:
            m_queue = deque([root])

            while m_queue:
                que_len = len(m_queue)
                level = []
                for _ in range(que_len):
                    cur = m_queue.popleft()
                    level.append(cur.val)
                    if cur.left: m_queue.append(cur.left)
                    if cur.right: m_queue.append(cur.right)
                r_list.append(level)

        return len(r_list)


if __name__ == '__main__':
    s = Solution_104()
