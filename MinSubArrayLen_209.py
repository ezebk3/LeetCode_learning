from typing import List


class Solution_209:

    def minSubArrayLen(self, target, nums):
        length = len(nums)
        left = 0
        right = 0
        min_len = length
        start, end = 0, -1
        while right < length:
            num = sum(nums[left:right + 1])
            if num < target:
                right += 1
            elif num >= target:
                if len(nums[left:right + 1]) <= min_len:
                    min_len = len(nums[left:right + 1])
                    start = left
                    end = right
                left += 1
        return len(nums[start:end + 1])

    def minSubArrayLen3(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        m_idx = len(nums) - 1
        min_len = float('inf')
        total = 0
        while left <= right and left <= m_idx and right <= m_idx:
            total += nums[right]
            while total >= target:
                length = right - left + 1
                if min_len > length:
                    min_len = length
                total -= nums[left]
                left += 1
            else:
                right += 1

        return 0 if min_len == float('inf') else min_len

    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0  # 用于跟踪当前窗口内的总和
        min_len = float('inf')  # 使用无穷大初始化最小长度

        for right in range(len(nums)):
            total += nums[right]  # 将当前元素添加到总和中
            while total >= target:  # 当总和大于等于目标值时，尝试缩小窗口
                min_len = min(min_len, right - left + 1)
                total -= nums[left]  # 从总和中减去窗口左边的元素
                left += 1  # 缩小窗口

        return min_len if min_len != float('inf') else 0


if __name__ == '__main__':
    s = Solution_209()
    r = s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
    print(r)
