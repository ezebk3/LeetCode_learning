class Solution_151:
    def reverseWords(self, s: str) -> str:
        str_arr = s.split(" ")
        rs = ""
        for str_sub in str_arr:
            if str_sub != '':
                rs = " " + str_sub + rs


        return rs[1:]


if __name__ == '__main__':
    s = Solution_151()
    print(s.reverseWords("a good   example"))
