from typing import List


class Solution_26:

    def removeDuplicates(self, nums: List[int]) -> int:
        idx = len(nums) - 1
        slow = 0
        fast = 1

        while fast <= idx:
            if nums[fast] != nums[slow]:
                nums[slow+1] = nums[fast]
                slow += 1
                fast += 1

            else:
                while fast <= idx and nums[fast] == nums[slow]:
                    fast += 1

        return slow+1


if __name__ == '__main__':
    s = Solution_26()

    r = s.removeDuplicates([1,1,2])

    print(r)
