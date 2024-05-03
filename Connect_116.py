"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution_116:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root:
            m_que = deque([root])

            while m_que:
                len_que = len(m_que)
                pre = None
                for _ in range(len_que):
                    cur = m_que.popleft()
                    if pre:
                        pre.next = cur
                    pre = cur
                    if cur.left:
                        m_que.append(cur.left)
                    if cur.right:
                        m_que.append(cur.right)
                    if _ == len_que - 1:
                        cur.next = None

        return root


if __name__ == '__main__':
    root = Node(val=1, left=Node(val=2, left=Node(4), right=Node(5)), right=Node(val=3, left=Node(6), right=Node(7)))
    s = Solution_116()
    s.connect(root)
