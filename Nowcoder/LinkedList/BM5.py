from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param lists ListNode类一维数组
# @return ListNode类
#
class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        new_head = ListNode(-1)
        cur = new_head

        p_vals = []
        for p in lists:
            if p:
                p_vals.append((p, p.val))

        while p_vals:
            s_p_vals = sorted(p_vals, key=lambda p_val: p_val[1])

            p_next = s_p_vals[0][0]
            cur.next = p_next
            p_next = p_next.next
            cur = cur.next
            if p_next:
                s_p_vals[0] = (p_next, p_next.val)
            else:
                del s_p_vals[0]
            p_vals = s_p_vals

        return new_head.next


if __name__ == '__main__':
    ph1 = ListNode(1)
    ph1.next = ListNode(3)
    ph1.next.next = ListNode(6)

    ph2 = ListNode(4)
    ph2.next = ListNode(7)
    ph2.next.next = ListNode(8)

    ph3 = ListNode(2)
    ph3.next = ListNode(5)
    ph3.next.next = ListNode(9)

    s = Solution()
    p = s.mergeKLists([ph1, ph2, ph3])
    while p:
        print(p.val)
        p = p.next
