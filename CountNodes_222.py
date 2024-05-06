# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        r_list = []
        if root:
            m_que = deque([root])
            while m_que:
                cur = m_que.pop()
                r_list.append(cur.val)
                if cur.right:
                    m_que.append(cur.right)
                if cur.left:
                    m_que.append(cur.left)

        return len(r_list)


if __name__ == '__main__':
    pass