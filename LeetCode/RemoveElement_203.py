# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


class Solution_203:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(val=-1, next=head)
        pre = dummy_head

        while pre.next:
            if pre.next.val != val:
                pre = pre.next
            else:
                pre.next = pre.next.next

        return dummy_head.next


if __name__ == '__main__':
    s = Solution_203()
    link = ListArr([7, 7, 7, 7])

    head = s.removeElements(head=link.Head, val=7)
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next
