import collections
import copy
from collections import defaultdict


class Solution_76:

    def checkCover(self, a, b):
        for key in b.keys():
            if key not in a.keys() or a[key] < b[key]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        target_dict = {}
        count_dict = {}
        left = 0
        min_len = float('inf')
        min_str = ""

        for i in t:
            if i not in target_dict.keys():
                target_dict[i] = 1
            else:
                target_dict[i] += 1

        for right, char_ in enumerate(s):
            if char_ in target_dict.keys():
                if char_ in count_dict.keys():
                    count_dict[char_] += 1
                else:

                    count_dict[char_] = 1

            while self.checkCover(count_dict, target_dict):
                if right - left + 1 < min_len:
                    min_str = s[left:right + 1]
                    min_len = right - left + 1

                if s[left] in target_dict.keys():
                    count_dict[s[left]] -= 1
                left += 1

        return min_str

    def minWindow2(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        target_dict = defaultdict(int)
        for char in t:
            target_dict[char] += 1

        count_dict = defaultdict(int)
        required = len(target_dict)
        formed = 0

        left, right = 0, 0
        min_len = float('inf')
        min_left = 0

        for right in range(len(s)):
            char = s[right]
            if char in target_dict:
                count_dict[char] += 1
                if count_dict[char] == target_dict[char]:
                    formed += 1

            while left <= right and formed == required:
                char = s[left]
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left

                if char in target_dict:
                    count_dict[char] -= 1
                    if count_dict[char] < target_dict[char]:
                        formed -= 1

                left += 1

        return "" if min_len == float('inf') else s[min_left:min_left + min_len]

    def minWindow3(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        target_dict = collections.defaultdict(int)
        count_dict = collections.defaultdict(int)
        left = 0
        min_len = float('inf')
        min_str = ""

        have_check = 0

        for i in t:
            target_dict[i] += 1

        need_check = len(target_dict)

        for right, char_ in enumerate(s):
            if char_ in target_dict.keys():
                count_dict[char_] += 1
                if count_dict[char_] == target_dict[char_]:
                    have_check += 1

            while have_check == need_check:
                char = s[left]
                if right - left + 1 < min_len:
                    min_str = s[left:right + 1]
                    min_len = right - left + 1

                if char in target_dict.keys():
                    count_dict[char] -= 1
                    if count_dict[char] < target_dict[char]:
                        have_check -= 1
                left += 1

        return min_str


if __name__ == '__main__':
    s = Solution_76()
    s1 = "ADOBECODEBANC"
    s2 = "ABC"
    r = s.minWindow3(s1, s2)
    print(r)
