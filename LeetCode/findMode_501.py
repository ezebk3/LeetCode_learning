# Definition for a binary tree node.
from typing import Optional, List
from tools.build_tree import MyTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.t_dict = {}

    def g_dict(self, root: Optional[TreeNode]):
        if root:
            if root.val in self.t_dict.keys():
                self.t_dict[root.val] += 1
            else:
                self.t_dict[root.val] = 1

            self.g_dict(root.left)
            self.g_dict(root.right)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.g_dict(root)
        val_list = sorted(self.t_dict.items(), key=lambda item: item[1],reverse=True)
        result_list = []
        for val_kv in val_list:
            if val_kv[1] == val_list[0][1]:
                result_list.append(val_kv[0])

        return result_list


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(val=1, left=None, right=TreeNode(val=2, right=None, left=TreeNode(val=2)))
    r = s.findMode(root)
    print(r)
