class Solution_383:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        cont_dict = {}

        for char_ in magazine:
            if char_ not in cont_dict.keys():
                cont_dict[char_] = 1
            else:
                cont_dict[char_] += 1

        for r in ransomNote:
            if r not in cont_dict.keys():
                return False
            elif cont_dict[r] <= 0:
                return False
            elif cont_dict[r] > 0:
                cont_dict[r] -= 1

        return True


if __name__ == '__main__':
    s = Solution_383()

    r = s.canConstruct("aa", "ab")
    print(r)
