"""
https://leetcode.com/problems/set-matrix-zeroes/
Given an m x n integer matrix matrix, if an element is 0, set its entire row
and column to 0's. You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1

Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
from typing import List

import pytest


class Solution:
    """
    Use sets to track columns and rows that needs to be filled
    Time: O(n*m)
    Space: O(n+m)
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        zero_rows = set()
        zero_cols = set()

        for row in range(num_rows):
            for col in range(num_cols):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)

        for row in range(num_rows):
            for col in range(num_cols):
                if row in zero_rows or col in zero_cols:
                    matrix[row][col] = 0


class Solution2:
    """
    Use first row and first column to store flags regarding column and row filling
    Time: O(n*m)
    Space: O(1)
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        fill_first_row = fill_first_col = False

        for row in range(num_rows):
            if matrix[row][0] == 0:
                fill_first_col = True

        for col in range(num_cols):
            if matrix[0][col] == 0:
                fill_first_row = True

        for row in range(1, num_rows):
            for col in range(1, num_cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        for row in range(1, num_rows):
            for col in range(1, num_cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if fill_first_col:
            for row in range(num_rows):
                matrix[row][0] = 0

        if fill_first_row:
            for col in range(num_cols):
                matrix[0][col] = 0


@pytest.mark.parametrize(
    "matrix,expected_output", (
        (
            [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
            [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
        ),
        (
            [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
            [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
        ),
    )
)
def test_set_zeroes(matrix, expected_output):
    Solution().setZeroes(matrix)
    assert matrix == expected_output
