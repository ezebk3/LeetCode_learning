class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @param m int整型
# @param n int整型
# @return ListNode类
#
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head:
            count = m - 1
            r_num = n - m + 1
            p = head
            start_link = None
            while count > 0:
                start_link = p
                p = p.next
                count -= 1

            start = p
            pre = None
            next_ = None
            while r_num > 0:
                next_ = p.next
                p.next = pre
                pre = p
                p = next_
                r_num -= 1

            if start_link:
                start_link.next = pre
                start.next = next_
                return head
            else:
                start.next = next_
                return pre
        else:
            return None

        # write code here


class Solution_2:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head:
            new_head = ListNode(-1)
            new_head.next = head

            pre = new_head
            cur = head
            for i in range(1, m):
                pre = cur
                cur = cur.next
            for i in range(m, n):
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            return new_head.next

        # write code here


if __name__ == '__main__':
    h = ListNode(1)
    h.next = ListNode(2)
    h.next.next = ListNode(3)
    h.next.next.next = ListNode(4)
    h.next.next.next.next = ListNode(5)
    s = Solution_2()
    p = s.reverseBetween(head=h, m=2, n=4)
    # h = ListNode(1)
    # h.next = ListNode(2)
    # # h.next.next = ListNode(3)
    # s = Solution()
    # p = s.reverseBetween(head=h, m=2, n=2)
    while p:
        print(p.val)
        p = p.next
