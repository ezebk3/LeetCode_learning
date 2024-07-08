class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


# @param head ListNode类
# @return bool布尔型
#
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head:
            fast_p = head
            slow_p = head
            while fast_p and fast_p.next:
                fast_p = fast_p.next.next
                slow_p = slow_p.next
                if fast_p == slow_p:
                    return True
            return False
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    s.hasCycle(head)
