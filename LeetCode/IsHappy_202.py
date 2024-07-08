class Solution_202:
    def get_sum(self, n):
        sum_ = 0
        while n > 0:
            sum_ += pow(n % 10, 2)
            n = n // 10

        return sum_

    def isHappy(self, n: int) -> bool:
        t_set = set()
        num_ = n
        while True:
            num_ = self.get_sum(num_)
            if num_ == 1:
                return True
            if num_ in t_set:
                return False
            else:
                t_set.add(num_)


if __name__ == '__main__':
    s = Solution_202()
    r = s.isHappy(19)
    print(r)
