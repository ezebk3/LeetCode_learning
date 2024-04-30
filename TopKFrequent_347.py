from typing import List


class Solution_347:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_count = {}

        for num in nums:
            if num not in dict_count.keys():
                dict_count[num] = 1
            else:
                dict_count[num] = dict_count[num] + 1

        f = zip(dict_count.values(), dict_count.keys())
        r = sorted(f)
        r_list = []
        for i in range(k):
            r_list.append(r[-(i + 1)][1])

        return r_list


if __name__ == '__main__':
    s = Solution_347()
    s.topKFrequent([1, 1, 1, 2, 2, 2, 2, 3], 2)
