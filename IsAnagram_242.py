class Solution_242:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0, ] * 26
        # arr[1] = 1
        for char_ in s:
            idx = ord(char_) - ord('a')
            arr[idx] += 1

        for char_ in t:
            idx = ord(char_) - ord('a')
            arr[idx] -= 1

        r = True

        for num in arr:
            if num != 0:
                r = False
                break

        return r


if __name__ == '__main__':
    s = Solution_242()
    r = s.isAnagram("rat", "car")
    print(r)
