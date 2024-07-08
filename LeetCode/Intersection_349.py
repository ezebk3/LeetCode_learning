from typing import List


class Solution_349:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        visit_arr = [False] * 1001
        for i in nums1:
            if visit_arr[i]:
                continue
            else:
                visit_arr[i] = True

        visit_result = []
        for i in nums2:
            if visit_arr[i]:
                visit_result.append(i)

        visit_result = list(set(visit_result))
        return visit_result


if __name__ == '__main__':
    s = Solution_349()
    r = s.intersection([1, 2, 2, 1], [2, 2])
    print(r)
