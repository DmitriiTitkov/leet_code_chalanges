"""
Write an efficient algorithm that searches for a value target in an m x n
integer matrix matrix. This matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example 1:
Input: matrix =
[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
target = 5
Output: true

Example 2:
Input: matrix =
[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
target = 20
Output: false


Constraints:
m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matrix[i][j] <= 109
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-109 <= target <= 109
"""
from typing import List

import pytest


class Solution:
    """
    Binary search solution.
    Time: O(n * logk)
    Space: O(1)
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_count = len(matrix)
        col_count = len(matrix[0])

        for row in range(row_count):
            l, r = 0, col_count - 1

            while l <= r:
                mid = (l + r) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

        return False


class Solution2:
    """
    Iterate from bottom left shrinking the matrix
    Time: O(n + m)
    Space: O(1)
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_count = len(matrix)
        col_count = len(matrix[0])

        row = row_count - 1
        col = 0

        while row >= 0 and col < col_count:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                col += 1
            else:
                row -= 1

        return False


@pytest.mark.parametrize(
    "solution", [Solution, Solution2]
)
@pytest.mark.parametrize(
    "matrix,target,expected_result", (
    (
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ],
        5,
        True
    ),
    (
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ],
        20,
        False
    )
)
)
def test_search_matrix(solution, matrix, target, expected_result):
    assert solution().searchMatrix(matrix, target) == expected_result
