from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

    def __repr__(self):
        return f"Node({self.val}, {self.isLeaf}, {self.topLeft}, {self.topRight}, {self.bottomLeft}, {self.bottomRight})"


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        def isAllSame(n, r, c):
            val = grid[r][c]
            for i in range(n):
                for j in range(n):
                    if val != grid[r + i][c + j]:
                        return False
            return True

        def dfs(n, r, c):
            if isAllSame(n, r, c):
                return Node(bool(grid[r][c]), True, None, None, None, None)

            half = n // 2
            topLeft = dfs(half, r, c)
            topRight = dfs(half, r, c + half)
            bottomLeft = dfs(half, r + half, c)
            bottomRight = dfs(half, r + half, c + half)
            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)

        return dfs(len(grid), 0, 0)

    # Optimal
    def construct_bottom_up(self, grid: List[List[int]]) -> "Node":
        def solve(n, r, c):
            if n == 1:
                return Node(grid[r][c] == 1, True, None, None, None, None)

            half = n // 2
            top_left = solve(half, r, c)
            top_right = solve(half, r, c + half)
            bottom_left = solve(half, r + half, c)
            bottom_right = solve(half, r + half, c + half)
            if (
                top_left.isLeaf
                and top_right.isLeaf
                and bottom_left.isLeaf
                and bottom_right.isLeaf
                and top_left.val == top_right.val == bottom_left.val == bottom_right.val
            ):
                return Node(top_left.val, True, None, None, None, None)

            return Node(True, False, top_left, top_right, bottom_left, bottom_right)

        return solve(len(grid), 0, 0)


if __name__ == "__main__":
    grid = [
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
    ]

    Solution().construct(grid)
    Solution().construct_bottom_up(grid)
