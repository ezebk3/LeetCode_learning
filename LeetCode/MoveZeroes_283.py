from typing import List


class Solution_283:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        max_idx = len(nums) - 1
        slow = 0
        fast = 0

        while fast <= max_idx:
            if nums[slow] == 0:
                while fast < max_idx and nums[fast] == 0:
                    fast += 1
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
                fast += 1
            else:
                slow += 1
                fast += 1




if __name__ == '__main__':
    s = Solution_283()
    s.moveZeroes([0,1,0,3,12])
