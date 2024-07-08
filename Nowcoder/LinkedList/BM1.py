class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def ReverseList(self, head: ListNode) -> ListNode:
        if head:
            pre = None
            p = head
            while p.next:
                if pre is None:
                    pre = p
                    p = p.next
                    pre.next = None

                else:
                    temp = p.next
                    p.next = pre
                    pre = p
                    p = temp

            p.next = pre
            return p
        else:
            return None
        # write code here


if __name__ == '__main__':
    s = Solution()
    head_ = ListNode(1)
    head_.next = ListNode(2)
    head_.next.next = ListNode(3)
    head_.next.next.next = ListNode(4)
    p = s.ReverseList(head_)
    while p:
        print(p.val)
        p = p.next
