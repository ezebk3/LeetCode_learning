class Solution_541:
    def subReverse(self, s: str):
        rd = ""
        for i in s:
            rd = i + rd

        return rd

    def reverseStr(self, s: str, k: int) -> str:

        num = len(s) // (2 * k)
        if num == 0:
            if len(s) < k:
                return self.subReverse(s)
            else:
                temp = self.subReverse(s[:k])
                return temp + s[k:]
        else:
            p_str = s[:2 * k * num]
            r_str = s[2 * k * num:]
            rs = ""
            for idx in range(num):
                sub = p_str[2 * k * idx:2 * k * (idx + 1)]
                temp = self.subReverse(sub[:k])
                temp = temp + sub[k:]
                rs = rs + temp

            if len(r_str) < k:
                return rs + self.subReverse(r_str)
            else:
                temp = self.subReverse(r_str[:k])
                return rs + temp + r_str[k:]


if __name__ == '__main__':
    s = Solution_541()

    r = s.reverseStr("abcdefg", 1)
    print(r)
