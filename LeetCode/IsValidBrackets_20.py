class Solution_20:
    def isValid(self, s: str) -> bool:
        str_arr = list(s)
        temp_queue = []

        for char_ in str_arr:
            if char_ == '(':
                temp_queue.append(')')
            elif char_ == '[':
                temp_queue.append(']')
            elif char_ == '{':
                temp_queue.append('}')
            elif char_ in [')', ']', '}']:
                if len(temp_queue) == 0:
                    return False

                if temp_queue[-1] == char_:
                    temp_queue.pop()
                else:
                    return False

        if len(temp_queue) > 0:
            return False

        return True


if __name__ == '__main__':
    s = Solution_20()
    print(s.isValid("]"))
