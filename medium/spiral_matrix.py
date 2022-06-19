"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
from typing import List

import pytest


class Solution:
    """Wordy solution that  has four boundaries and separate logic for each
    direction
    Time: O(n*m)
    Space: O(1)
    n - number of columns
    m - number of rows
    """

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        first_row = 0
        first_col = 0
        last_row = len(matrix) - 1
        last_col = len(matrix[0]) - 1

        spiral_order = []
        direction = "r"
        while first_row <= last_row and first_col <= last_col:
            if direction == "r":
                cur_col = first_col
                while cur_col <= last_col:
                    spiral_order.append(matrix[first_row][cur_col])
                    cur_col += 1
                first_row += 1
                direction = "d"
            elif direction == "d":
                cur_row = first_row
                while cur_row <= last_row:
                    spiral_order.append(matrix[cur_row][last_col])
                    cur_row += 1
                last_col -= 1
                direction = "l"

            elif direction == "l":
                cur_col = last_col
                while cur_col >= first_col:
                    spiral_order.append(matrix[last_row][cur_col])
                    cur_col -= 1
                last_row -= 1
                direction = "u"

            elif direction == "u":
                cur_row = last_row
                while cur_row >= first_row:
                    spiral_order.append(matrix[cur_row][first_col])
                    cur_row -= 1
                first_col += 1
                direction = "r"

        return spiral_order


@pytest.mark.parametrize(
    "matrix,expected_output",(
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
        ),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ),
    )

)
def test_spiral_matrix(matrix, expected_output):
    assert Solution().spiralOrder(matrix) == expected_output
