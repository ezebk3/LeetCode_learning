class Solution_367:
    def isPerfectSquare(self, x: int) -> int:
        right = 2 ** 32
        left = 0
        while left <= right:
            middle = left + (right - left) // 2

            if middle * middle == x:
                return True
            elif middle * middle > x:
                right = middle - 1
            else:
                left = middle + 1

        return False


if __name__ == '__main__':
    s = Solution_367()

    r = s.isPerfectSquare(4)

    print(r)
