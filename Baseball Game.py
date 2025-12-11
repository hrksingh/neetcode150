from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack, res = [], 0

        for op in operations:
            if op == "+":
                # 1. Calculate the new score (sum of the last two valid scores)
                new_score = stack[-1] + stack[-2]

                # 2. Update the running total
                res += new_score

                # 3. Add the *new score* (NOT res) to the record stack
                stack.append(new_score)

            elif op == "D":
                # 1. Calculate the new score (double the last valid score)
                new_score = 2 * stack[-1]

                # 2. Update the running total
                res += new_score

                # 3. Add the *new score* (NOT res) to the record stack
                stack.append(new_score)

            elif op == "C":
                # It correctly updates res and pops the stack
                res -= stack[-1]
                stack.pop()

            else:
                # It correctly updates res and appends the score
                score = int(op)
                res += score
                stack.append(score)

        return res
