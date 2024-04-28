from typing import List


class Solution_15:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        count_dict = {}

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                key_num = nums[i] + nums[j]
                if key_num not in count_dict.keys():
                    count_dict[key_num] = [[i, j]]
                else:
                    count_dict[key_num].append([i, j])

        result = []
        for idx, num in enumerate(nums):
            to_find = 0 - num
            if idx + 1 < len(nums) and nums[idx] == num[idx + 1]:
                continue
            if to_find in count_dict.keys():
                arr = count_dict[to_find]
                for pair in arr:
                    if idx not in pair:
                        n_list = [nums[idx], nums[pair[0]], nums[pair[1]]]
                        n_list.sort()
                        if n_list not in result:
                            result.append(n_list)
        return result


if __name__ == '__main__':
    s = Solution_15()
    s.threeSum([-1, 0, 1, 2, -1, -4])
