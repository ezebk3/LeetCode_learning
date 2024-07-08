# Definition for a binary tree node.
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution_637:

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        r_list = []
        if root:
            m_queue = deque([root])

            while m_queue:
                level_total = 0
                level_len = len(m_queue)
                for _ in range(level_len):
                    cur = m_queue.popleft()
                    if cur.left:
                        m_queue.append(cur.left)
                    if cur.right:
                        m_queue.append(cur.right)
                    level_total += cur.val

                r_list.append(level_total / level_len)

        return r_list


if __name__ == '__main__':
    s = Solution_637()
    root = TreeNode(val=1, left=TreeNode(val=2, right=TreeNode(val=5, right=TreeNode(val=6))),
                    right=TreeNode(val=3, right=TreeNode(val=4)))
    print(s.averageOfLevels(root))
