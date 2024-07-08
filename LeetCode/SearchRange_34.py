from typing import List


class Solution_34:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        tar_idx = -1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                tar_idx = mid
                break

        if tar_idx == -1:
            return [-1, -1]
        else:
            left_idx = tar_idx
            right_idx = tar_idx
            while left_idx > 0 and nums[left_idx - 1] == target:
                left_idx -= 1

            while right_idx < len(nums) - 1 and nums[right_idx + 1] == target:
                right_idx += 1

            return [left_idx, right_idx]


if __name__ == '__main__':
    s = Solution_34()
    r = s.searchRange([1], 1)
    print(r)
