class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.dummy_head = ListNode()
        self.length = 0

    def get(self, index: int) -> int:
        if index > self.length - 1:
            return -1
        else:
            cur = self.dummy_head.next
            for i in range(index + 1):
                if i == index:
                    return cur.val
                else:
                    cur = cur.next

    def addAtHead(self, val: int) -> None:
        temp = self.dummy_head.next
        self.dummy_head.next = ListNode(val=val, next=None)
        self.dummy_head.next.next = temp
        self.length += 1

    def addAtTail(self, val: int) -> None:
        pre = self.dummy_head
        while pre.next:
            pre = pre.next

        pre.next = ListNode(val)
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return None

        pre = self.dummy_head
        for i in range(index + 1):
            if i == index:
                temp = pre.next
                pre.next = ListNode(val)
                pre.next.next = temp
            else:
                pre = pre.next

        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index > self.length:
            return None

        pre = self.dummy_head
        for i in range(index + 1):
            if i == index:
                pre.next = pre.next.next
            else:
                pre = pre.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

if __name__ == '__main__':
    # mll = MyLinkedList()
    # mll.addAtHead(7)
    # mll.addAtHead(2)
    # mll.addAtHead(1)
    # mll.addAtIndex(3, 0)
    # mll.deleteAtIndex(2)
    # mll.addAtHead(6)
    # mll.addAtTail(4)
    # mll.get(4)
    # mll.addAtHead(4)
    # mll.addAtIndex(5, 0)
    # mll.addAtHead(6)

    mll = MyLinkedList()
    mll.addAtTail(1)
    mll.get(0)