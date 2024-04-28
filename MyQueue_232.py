class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                self.out_stack.append(self.in_stack.pop())
            return self.out_stack.pop()
        else:
            return self.out_stack.pop()

    def peek(self) -> int:
        pass

    def empty(self) -> bool:
        pass


def stack_t():
    t_list = [1, 2, 3, 4]
    t_list.pop(0)
    print(t_list)


if __name__ == '__main__':
    stack_t()
