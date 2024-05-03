"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from typing import List
from collections import deque


class Solution_429:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        r_list = []
        if root:
            m_que = deque([root])
            while m_que:
                que_len = len(m_que)
                level = []
                for i in range(que_len):
                    cur = m_que.popleft()
                    level.append(cur.val)

                    if cur.children:
                        for child in cur.children:
                            m_que.append(child)

                r_list.append(level)

        return r_list


if __name__ == '__main__':
    s = Solution_429()
    root = Node(val=1, children=[Node(val=3, children=[Node(val=5), Node(val=6)]), Node(val=2), Node(val=4)])
    print(s.levelOrder(root))
