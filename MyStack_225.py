class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0


if __name__ == '__main__':
    s = MyStack()

    s.push(1)
    s.push(2)
    s.push(3)
    a = s.pop()

    a = s.pop()
    a = s.pop()
    print(s.empty())
