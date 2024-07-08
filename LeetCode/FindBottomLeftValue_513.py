# Definition for a binary tree node.
from typing import Optional
from collections import deque
from gen_Tree import MyTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root:
            my_que = deque([root])
            r_list = []
            while my_que:
                level = []
                row_num = len(my_que)
                for _ in range(row_num):
                    cur = my_que.popleft()
                    level.append(cur.val)
                    if cur.left:
                        my_que.append(cur.left)
                    if cur.right:
                        my_que.append(cur.right)
                r_list.append(level)
            last_level = r_list[-1]
            last_val = last_level[0]
            return last_val
        else:
            return -1


if __name__ == '__main__':
    root = MyTree([2, 1, 3]).root
    s = Solution()
    print(s.findBottomLeftValue(root))
