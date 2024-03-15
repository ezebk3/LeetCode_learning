from typing import List


class Solution_495:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total_duration = 0

        before_attack_end = 0
        for t in timeSeries:
            t_end = t + duration - 1

            if t > before_attack_end:
                total_duration += duration
            else:
                total_duration += t_end - before_attack_end

            before_attack_end = t_end

        return total_duration


if __name__ == '__main__':
    s = Solution_495()
    timeSeries_ = [1,4]
    duration_ = 2

    r = s.findPoisonedDuration(timeSeries_, duration_)
    print(r)
