from typing import List


class Solution_1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_count = {}

        for idx, num in enumerate(nums):
            to_find = target - num
            if num in dict_count.keys():
                return [idx, dict_count[num]]
            else:
                dict_count[to_find] = idx

        return []


if __name__ == '__main__':
    s = Solution_1()
    r = s.twoSum([2,7,11,15], 9)
    print(r)
