class Solution_844:
    def get_subSeq(self, s: str):
        fast_s = 0
        slow_s = 0

        while fast_s <= len(s) - 1:
            if s[fast_s] != "#":
                slow_s += 1
                fast_s += 1
            else:
                slow_s = max(0, slow_s - 1)
                fast_s += 1
                s = s[:slow_s] + s[fast_s:]
                fast_s = max(0, fast_s - 2)

        return s

    def backspaceCompare(self, s: str, t: str) -> bool:
        sub_s = self.get_subSeq(s)
        sub_t = self.get_subSeq(t)
        if len(sub_t) != len(sub_s):
            return False
        else:
            for i in range(len(sub_s)):
                if sub_t[i] != sub_s[i]:
                    return False

            return True


if __name__ == '__main__':
    s = Solution_844()
    r = s.backspaceCompare("a##c", "#a#c")
    print(r)
