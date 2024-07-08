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


class Solution_19:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        slow = dummy_head
        fast = dummy_head

        count = n

        while count > 0:
            fast = fast.next
            count -= 1

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy_head.next


if __name__ == '__main__':
    s = Solution_19()

    mylist = ListArr([1, 2])

    mylist = s.removeNthFromEnd(mylist.Head, 2)

    p = mylist
    while p:
        print(p.val)
        p = p.next
