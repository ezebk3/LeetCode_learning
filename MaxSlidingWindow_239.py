from typing import List
from collections import deque


class MyQueue:
    def __init__(self):
        self.t_queue = deque()

    def push(self, val):
        if len(self.t_queue) == 0:
            self.t_queue.append(val)
            return

        if self.t_queue[-1] > val:
            self.t_queue.append(val)
        else:
            while len(self.t_queue) > 0 and self.t_queue[-1] < val:
                self.t_queue.pop()
            self.t_queue.append(val)

    def pop(self, val):
        if val == self.t_queue[0]:
            self.t_queue.popleft()

    def front(self):
        return self.t_queue[0]


class Solution_239:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = MyQueue()
        max_list = []
        for i in range(k):
            que.push(nums[i])
        max_list.append(que.front())

        for i in range(k, len(nums)):
            que.pop(nums[i - k])
            que.push(nums[i])
            max_list.append(que.front())

        return max_list


if __name__ == '__main__':
    s = Solution_239()
    print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
