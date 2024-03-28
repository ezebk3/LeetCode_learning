# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution_142:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        slow = head
        fast = head
        have_loop = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                have_loop = True
                break

        if not have_loop:
            return None

        p1 = head
        p2 = fast
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1


if __name__ == '__main__':
    # [3,2,0,-4]
    l1 = ListNode(3)
    l2 = ListNode(2)
    l3 = ListNode(0)
    l4 = ListNode(-4)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l2
    s = Solution_142()
    l = s.detectCycle(l1)
    print(l.val)
