class Solution_459:
    def getNext(self, s):
        nxt = [0] * len(s)
        nxt[0] = -1
        j = -1
        for i in range(1, len(s)):
            while j >= 0 and s[i] != s[j + 1]:
                j = nxt[j]
            if s[i] == s[j + 1]:
                j += 1
            nxt[i] = j
        return nxt

    def get_next_arr(self, pattern):
        next_arr = [0]
        i = 0
        j = 1
        while len(next_arr) < len(pattern):
            if pattern[i] == pattern[j]:
                i += 1
                j += 1
                next_arr.append(i)
            else:
                if i == 0:
                    next_arr.append(i)
                    j += 1
                else:
                    i = next_arr[i - 1]

        return next_arr

    def repeatedSubstringPattern(self, s: str) -> bool:
        next_arr = self.get_next_arr(s)
        print(next_arr)

        if next_arr[-1] != 0 and len(s) % (len(s) - next_arr[-1]) == 0:
            return True
        return False


class Solution_v2:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ss = s + s
        rs = ss.find(s, 1)
        return rs != len(s)


if __name__ == '__main__':
    s = Solution_v2()
    r = s.repeatedSubstringPattern("abab")
    print(r)
