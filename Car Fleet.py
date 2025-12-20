from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position, speed), reverse=True)

        for pos, s in cars:
            t = (target - pos) / s

            if not stack or stack[-1] < t:
                stack.append(t)
        return len(stack)


if __name__ == "__main__":
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]

    print(Solution().carFleet(target, position, speed))
