from typing import List


class Solution_150:
    def evalRPN(self, tokens: List[str]) -> int:
        t_stack = []
        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                post = t_stack.pop()
                pre = t_stack.pop()
                if t == "+":
                    t_stack.append(pre + post)
                elif t == "-":
                    t_stack.append(pre - post)
                elif t == "*":
                    t_stack.append(pre * post)
                elif t == "/":
                    if pre / post > 0:
                        t_stack.append(pre // post)
                    else:
                        t_stack.append(-(-pre // post))
            else:
                t_stack.append(int(t))
        return t_stack[-1]


if __name__ == '__main__':
    s = Solution_150()
    print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
