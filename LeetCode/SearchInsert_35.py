from typing import List


class Solution_35:

    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if target > nums[right]:
            return right + 1
        elif target < nums[left]:
            return 0
        else:

            while left <= right:
                middle = left + (right - left) // 2
                if nums[middle] == target:
                    return middle

                elif nums[middle] > target:
                    right = middle - 1
                else:
                    left = middle + 1

            return left


if __name__ == '__main__':
    s = Solution_35()
    r = s.searchInsert([1, 3, 5, 6], 7)
    print(r)
