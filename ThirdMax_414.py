from typing import List


class Solution_414:
    def thirdMax(self, nums: List[int]) -> int:
        first_ = -2 ** 31
        second_ = -2 ** 31
        third_ = -2 ** 31

        nums = set(nums)
        if len(nums) < 3:
            return max(nums)

        arr = [first_, second_, third_]
        for i in nums:
            if i >= min(arr):
                arr.remove(min(arr))
                arr.append(i)

        max_v = max(arr)
        arr.remove(max_v)
        if arr[0] == arr[1]:
            return max_v
        else:
            return min(arr)


if __name__ == '__main__':
    s = Solution_414()
    r = s.thirdMax([2, 2, 3, 1])
    print(r)
