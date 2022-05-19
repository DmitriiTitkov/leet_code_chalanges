"""
Given an m x n integers matrix, return the length of the longest increasing
path in matrix. From each cell, you can either move in four directions:
left, right, up, or down. You may not move diagonally or move outside the
boundary (i.e., wrap-around is not allowed).

Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is
not allowed.

Example 3:
Input: matrix = [[1]]
Output: 1

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
"""
from functools import cache
from typing import List

import pytest


class Solution:
    """
    DFS+memorization solution to find max lengths of increasing paths
    Time: O(n*m)
    Space: O(n*m)
    """
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        num_rows, num_cols = len(matrix), len(matrix[0])

        @cache
        def dfs(row: int, col: int) -> int:
            max_increasing_path = 0

            for r, c in (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1):
                if (0 <= r < num_rows and 0 <= c < num_cols and
                        matrix[r][c] > matrix[row][col]):
                    max_increasing_path = max(max_increasing_path, dfs(r, c))

            return max_increasing_path + 1

        max_increasing_path = 1
        for row in range(num_rows):
            for col in range(num_cols):
                max_increasing_path = max(dfs(row, col), max_increasing_path)

        return max_increasing_path


@pytest.mark.parametrize(
    "matrix,expected_output",
    (
        ([[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4),
        ([[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4),
        ([[1]], 1),
    )
)
def test_longest_increasing_path(matrix, expected_output):
    assert Solution().longestIncreasingPath(matrix) == expected_output
