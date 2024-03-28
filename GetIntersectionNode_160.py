# Definition for singly-linked list.
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


class Solution_160:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        if headA == headB:
            return headA

        n = 1
        m = 1

        p_A = headA
        p_B = headB

        while p_A.next:
            n += 1
            p_A = p_A.next

        while p_B.next:
            m += 1
            p_B = p_B.next

        if n > m:
            p_A = headA
            p_B = headB
        else:
            p_A = headB
            p_B = headA

        count = 0
        while count < abs(n - m):
            p_A = p_A.next
            count += 1

        while p_A:
            if p_A == p_B:
                return p_A
            p_A = p_A.next
            p_B = p_B.next

        return None


if __name__ == '__main__':
    s = Solution_160()

    l1 = ListArr([3])
    l2 = ListArr([2,3])

    r = s.getIntersectionNode(l1.Head, l2.Head)
    print(r.val)
