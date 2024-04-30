class MyQueue:

    def __init__(self):
        self.__in_stack = []
        self.__out_stack = []

    def push(self, x: int) -> None:
        self.__in_stack.append(x)

    def pop(self) -> int:
        if len(self.__out_stack) == 0:
            while len(self.__in_stack) > 0:
                self.__out_stack.append(self.__in_stack.pop())
            return self.__out_stack.pop()
        else:
            return self.__out_stack.pop()

    def peek(self) -> int:
        if len(self.__out_stack) == 0:
            while len(self.__in_stack) > 0:
                self.__out_stack.append(self.__in_stack.pop())
            return self.__out_stack[-1]
        else:
            return self.__out_stack[-1]

    def empty(self) -> bool:
        return len(self.__out_stack) + len(self.__in_stack) == 0


def stack_t():
    t_list = [1, 2, 3, 4]
    t_list.pop(0)
    print(t_list)


if __name__ == '__main__':
    qq = MyQueue()
    qq.push(1)
    qq.push(2)
    qq.push(3)
    qq.pop()
    qq.pop()
    qq.peek()
