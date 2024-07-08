class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListArr:

    def __init__(self, arr):
        self.Head = None
        pre = None
        for i in arr:
            if self.Head:
                pre.next = ListNode(i)
                pre = pre.next
            else:
                self.Head = ListNode(i)
                pre = self.Head
