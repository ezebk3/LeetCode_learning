class Solution_28:

    def get_next(self, pattern):
        next_val = [0]
        j = 1
        i = 0
        while len(next_val) < len(pattern):
            if pattern[j] == pattern[i]:
                i += 1
                next_val.append(i)
                j += 1
            else:
                if i == 0:
                    next_val.append(i)
                    j += 1
                else:
                    i = next_val[i - 1]

        next_val.insert(0, -1)
        del next_val[-1]
        return next_val

    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        next_arr = self.get_next(needle)
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j
            else:
                j = next_arr[j]
                if j == -1:
                    i += 1
                    j = 0
        return -1


if __name__ == '__main__':
    s = Solution_28()
    needle_ = "leeto"
    main_str = "leetcode"
    r = s.strStr(main_str, needle_)
    print(r)
