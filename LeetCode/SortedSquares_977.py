from typing import List


class Solution_977:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        right = len(nums) - 1
        left = 0
        temp = [None] * len(nums)
        idx = len(nums) - 1
        while right >= left:
            if abs(nums[right]) > abs(nums[left]):
                temp[idx] = nums[right] * nums[right]
                right -= 1
                idx -= 1
            else:
                temp[idx] = nums[left] * nums[left]
                left += 1
                idx -= 1

        print(temp)
        return temp


if __name__ == '__main__':
    s = Solution_977()
    s.sortedSquares([-3, -3, -2, 1])
