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
        top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        left = 0

        row = col = 0
        spiral_order = []
        direction = 'r'

        while len(spiral_order) < len(matrix) * len(matrix[0]):
            spiral_order.append(matrix[row][col])
            if direction == 'r':
                if col < right:
                    col += 1
                else:
                    top += 1
                    row += 1
                    direction = 'd'
            elif direction == 'd':
                if row < bottom:
                    row += 1
                else:
                    right -= 1
                    col -= 1
                    direction = 'l'
            elif direction == 'l':
                if col > left:
                    col -= 1
                else:
                    bottom -= 1
                    row -= 1
                    direction = 'u'
            elif direction == 'u':
                if row > top:
                    row -= 1
                else:
                    left += 1
                    col += 1
                    direction = 'r'

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
