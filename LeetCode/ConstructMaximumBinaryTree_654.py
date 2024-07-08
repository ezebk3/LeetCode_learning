# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution_654:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) > 0:
            root_num = max(nums)
            root_num_idx = nums.index(root_num)
            left_tree_list = nums[0:root_num_idx]
            right_tree_list = nums[root_num_idx + 1:]
            root = TreeNode(val=root_num)
            root.left = self.constructMaximumBinaryTree(left_tree_list)
            root.right = self.constructMaximumBinaryTree(right_tree_list)
            return root
        else:
            return None
