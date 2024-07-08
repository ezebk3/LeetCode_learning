# Definition for a binary tree node.
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution_515:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        r_list = []
        if root:
            m_que = deque([root])

            while m_que:
                level_max = -(2 ** 32)
                que_len = len(m_que)
                for _ in range(que_len):
                    cur = m_que.popleft()
                    if cur.val > level_max:
                        level_max = cur.val

                    if cur.left:
                        m_que.append(cur.left)
                    if cur.right:
                        m_que.append(cur.right)

                r_list.append(level_max)
        return r_list


if __name__ == '__main__':
    s = Solution_515()
    root = TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)))
    print(s.largestValues(root))
