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


class NumMatrix2:
    """
    Calculate 2D rolling sum for columns and rows. Than exclude areas outside of
    boundaries of region in question. We need to add top-left area back as it
    was excluded twice.

    Construct matrix:
        Time: O(nm)
        Space: O(nm)

    sumRegion:
        Time: O(1)
        Space: O(1)

    n - number of rows
    m - number of columns
    """
    def __init__(self, matrix: List[List[int]]):
        self.num_rows = len(matrix)
        self.num_cols = len(matrix[0])

        self._roll_sum = [[0] * (self.num_cols + 1) for row in range(self.num_rows + 1)]
        for row in range(1, self.num_rows + 1):
            row_roll_sum = 0
            for col in range(1, self.num_cols + 1):
                row_roll_sum += matrix[row - 1][col - 1]
                self._roll_sum[row][col] = row_roll_sum + self._roll_sum[row - 1][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rs = self._roll_sum
        return rs[row2 + 1][col2 + 1] - rs[row1][col2 + 1] - rs[row2 + 1][col1] + rs[row1][col1]