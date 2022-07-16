"""
There is an m x n grid with a ball. The ball is initially at the position
[startRow, startColumn]. You are allowed to move the ball to one of the four
adjacent cells in the grid (possibly out of the grid crossing the grid boundary).
You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number
of paths to move the ball out of the grid boundary. Since the answer can be
very large, return it modulo 109 + 7.

Example 1:
Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6

Example 2:
Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12

Constraints:
1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n
"""
from functools import cache

import pytest


class Solution:
    """
    Traverse all direction until out of boundaries
    Time: O(m*n*k)
    Space: O(m*n*k)

    k - maxMove
    """
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        @cache
        def find_paths_rec(row: int, col: int, moves_left: int) -> int:
            if row < 0 or col < 0 or row == m or col == n:
                return 1
            elif moves_left == 0:
                return 0

            total_paths = 0
            for r, c in (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1):
                total_paths += find_paths_rec(r, c, moves_left - 1)

            return total_paths % (10 ** 9 + 7)

        return find_paths_rec(startRow, startColumn, maxMove)


@pytest.mark.parametrize(
    "m,n,maxMove,startRow,startColumn,expected_output", (
            (2, 2, 2, 0, 0, 6),
            (1, 3, 3, 0, 1, 12),
    )
)
def test_find_paths(m, n, maxMove, startRow, startColumn, expected_output):
    assert Solution().findPaths(m, n, maxMove, startRow, startColumn, ) == expected_output
