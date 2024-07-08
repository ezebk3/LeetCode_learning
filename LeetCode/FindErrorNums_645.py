from typing import List


class Solution_645:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = [0 for i in range(max(nums) + 2)]
        # nums.sort()
        dup = 0
        for item in nums:
            count[item] += 1
            if count[item] > 1:
                dup = item
                break
        # if item != idx + 1:
        #     loss_num = idx + 1

        loss = 0
        for idx, item in enumerate(count):
            if idx != 0 and item == 0:
                loss = idx
                break
        return [dup, loss]
    # print(result)


if __name__ == '__main__':
    s = Solution_645()
    # r = s.findErrorNums([1, 5, 3, 2, 2, 7, 6, 4, 8, 9])
    r = s.findErrorNums([3,3,1])
    print(r)
