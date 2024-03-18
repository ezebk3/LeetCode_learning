# Definition for singly-linked list.
from typing import Optional


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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution_206:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        new_head = ListNode(next=None)
        while cur:
            temp = cur
            cur = cur.next

            temp.next = new_head.next
            new_head.next = temp

        return new_head.next


if __name__ == '__main__':
    la = ListArr([1, 2, 3, 4, 5])
    s = Solution_206()
    p = s.reverseList(la.Head)
    while p:
        print(p.val)
        p = p.next
