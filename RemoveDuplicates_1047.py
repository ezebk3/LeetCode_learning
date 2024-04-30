class Solution_1047:
    def removeDuplicates(self, s: str) -> str:
        t_stack = [-1]
        s_arr = list(s)
        for char_ in s_arr:
            if t_stack[-1] == char_:
                t_stack.pop()
            else:
                t_stack.append(char_)

        t_stack.pop(0)
        return ''.join(t_stack)


if __name__ == '__main__':
    s = Solution_1047()
    print(s.removeDuplicates("abbaca"))
