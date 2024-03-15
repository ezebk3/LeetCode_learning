from typing import List


class Solution_904:
    def totalFruit(self, fruits: List[int]) -> int:
        max_len = 0
        left = 0
        basket = []
        temp_len = 0
        for i in range(len(fruits)):
            if fruits[i] not in basket:
                if len(set(basket)) >= 2:

                    f_fruit = set(basket) - set([fruits[i - 1]])
                    f_fruit = f_fruit.pop()
                    while f_fruit in basket:
                        left += 1
                        temp_len -= 1
                        del basket[0]

                    basket.append(fruits[i])
                    temp_len += 1
                    max_len = max(max_len, temp_len)
                else:
                    basket.append(fruits[i])
                    temp_len += 1
                    max_len = max(max_len, temp_len)
            elif fruits[i] in basket:
                basket.append(fruits[i])
                temp_len += 1
                max_len = max(max_len, temp_len)

        return max_len

    def totalFruit2(self, fruits: List[int]) -> int:
        max_len = 0
        left = 0
        basket = {}
        for i in range(len(fruits)):
            if fruits[i] not in basket.keys():
                basket[fruits[i]] = 1
            else:
                basket[fruits[i]] += 1
            if len(basket) <= 2:
                max_len = max(max_len, i - left + 1)
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

        return max_len


if __name__ == '__main__':
    s = Solution_904()
    r = s.totalFruit2([1, 0, 1, 4, 1, 4, 1, 2, 3])
    print(r)
