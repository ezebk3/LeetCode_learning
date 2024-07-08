# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


class Solution_24:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy_head = ListNode(next=head)
        cur = dummy_head
        first = True
        while cur.next and cur.next.next:
            one = cur.next
            two = cur.next.next
            if first:
                dummy_head.next = two
                first = False
            one.next = two.next
            two.next = one
            cur.next = two
            cur = one
        return dummy_head.next


if __name__ == '__main__':
    s = Solution_24()
    ls = ListArr([1])
    s.swapPairs(ls.Head)
