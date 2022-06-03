"""
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its
upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:
NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the
elements of matrix inside the rectangle defined by its upper left corner
(row1, col1) and lower right corner (row2, col2).

Example 1:
Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[
    [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ],

    [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]
]
Output
[null, 8, 11, 12]
Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1],
[1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-105 <= matrix[i][j] <= 105
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 104 calls will be made to sumRegion.
"""
from typing import List

import pytest


class NumMatrix:
    """Calculate rolling sum for all rows so range can be calculated in O(1).
    Then sum the values for all ranges in all rows.

    Construct matrix:
        Time: O(nm)
        Space: O(nm)

    sumRegion:
        Time: O(m)
        Space: O(1)

    n - number of rows
    m - number of columns
    """
    def __init__(self, matrix: List[List[int]]):
        self.num_rows = len(matrix)
        self.num_cols = len(matrix[0])

        self._rolling_sum_mat = [[0] * self.num_cols for row in range(self.num_rows)]
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if col == 0:
                    self._rolling_sum_mat[row][col] = matrix[row][col]
                else:
                    self._rolling_sum_mat[row][col] = (
                            self._rolling_sum_mat[row][col - 1] + matrix[row][col]
                    )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        region_sum = 0

        for row in range(row1, row2 + 1):
            row_sum = self._rolling_sum_mat[row][col2]
            if col1 > 0:
                row_sum -= self._rolling_sum_mat[row][col1 - 1]

            region_sum += row_sum

        return region_sum

