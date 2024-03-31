from typing import List


class Solution_454:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count_dict = {}

        for num1 in nums1:
            for num2 in nums2:
                key_num = num1 + num2
                if key_num in count_dict.keys():
                    count_dict[key_num] += 1
                else:
                    count_dict[key_num] = 1

        count_zero = 0
        for num3 in nums3:
            for num4 in nums4:
                to_find = 0 - num3 - num4
                if to_find in count_dict.keys():
                    count_zero += count_dict[to_find]

        return count_zero


if __name__ == '__main__':
    s = Solution_454()
