from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        # create prefix_matrix
        self.prefixMatrix = [
            [0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)
        ]

        for r in range(1, len(self.prefixMatrix)):
            for c in range(1, len(self.prefixMatrix[0])):
                self.prefixMatrix[r][c] = (
                    self.prefixMatrix[r - 1][c]  # above
                    + self.prefixMatrix[r][c - 1]  # left
                    - self.prefixMatrix[r - 1][c - 1]  # top-left overlap
                    + matrix[r - 1][c - 1]  # current element in original
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefixMatrix[row2 + 1][col2 + 1]
            - self.prefixMatrix[row1][col2 + 1]
            - self.prefixMatrix[row2 + 1][col1]
            + self.prefixMatrix[row1][col1]
        )


# matrix = [
#     [1, 2, -1, -3, 4, 2, 0, 1],
#     [3, -2, 4, 5, -3, -1, 1, 0],
#     [0, 1, -3, 1, 3, 2, 4, -2],
#     [-1, 3, 4, 7, -2, 0, 1, 3],
#     [3, 4, 2, 4, -7, -1, 3, 0],
#     [-5, 4, 1, -2, 3, -4, 3, 3],
# ]
