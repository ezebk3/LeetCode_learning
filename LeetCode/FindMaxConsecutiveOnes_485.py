from typing import List


class Solution_485:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        temp_count = 0
        for idx in range(len(nums)):
            if nums[idx] == 1:
                temp_count += 1
            else:
                if temp_count > max_count:
                    max_count = temp_count
                    temp_count = 0

        if temp_count > max_count:
            max_count = temp_count

        return max_count


if __name__ == '__main__':
    s = Solution_485()
    nums = []

    print("len:{}".format(len(nums)))

    r = s.findMaxConsecutiveOnes(nums)
    print(r)
