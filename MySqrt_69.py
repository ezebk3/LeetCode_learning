class Solution_69:
    def mySqrt(self, x: int) -> int:
        right = 2 ** 32
        left = 0
        while left <= right:
            middle = left + (right - left) // 2

            if middle * middle == x:
                return middle
            elif middle * middle > x:
                right = middle - 1
            else:
                left = middle + 1

        return right


if __name__ == '__main__':
    s = Solution_69()

    r = s.mySqrt(4)

    print(r)
