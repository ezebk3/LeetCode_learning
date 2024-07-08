class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#
class Solution:
    def Merge(self, pHead1: ListNode, pHead2: ListNode) -> ListNode:
        if pHead1 and pHead2:
            dummy_head = ListNode(-1)
            cur = dummy_head

            while pHead1 and pHead2:
                if pHead1.val < pHead2.val:
                    cur.next = pHead1
                    pHead1 = pHead1.next
                else:
                    cur.next = pHead2
                    pHead2 = pHead2.next

                cur = cur.next

            if pHead1:
                cur.next = pHead1
            if pHead2:
                cur.next = pHead2
            return dummy_head.next
        elif pHead1:
            return pHead1
        elif pHead2:
            return pHead2
        else:
            return pHead1


if __name__ == '__main__':
    ph1 = ListNode(1)
    ph1.next = ListNode(3)
    ph1.next.next = ListNode(6)

    ph2 = ListNode(4)
    ph2.next = ListNode(7)
    ph2.next.next = ListNode(8)

    s = Solution()
    p = s.Merge(ph1, ph2)
    while p:
        print(p.val)
        p = p.next
    # write code here
