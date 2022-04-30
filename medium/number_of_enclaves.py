"""
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1
represents a land cell. A move consists of walking from one land cell to
another adjacent (4-directionally) land cell or walking off the boundary of the
grid.

Return the number of land cells in grid for which we cannot walk off the
boundary of the grid in any number of moves.

Example 1:
Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not
enclosed because its on the boundary.

Example 2:
Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.
"""
from typing import List

import pytest


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(row, col) -> int:
            visited.add((row, col))
            res = 1

            moves = (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)

            for r, c in moves:
                if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
                    if grid[r][c] == 0 or (r, c) in visited:
                        continue

                    res += dfs(r, c)

            return res

        # run for grid edge cells
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if row in (0, len(grid) - 1) or col in (0, len(grid[row]) - 1):
                    if grid[row][col] == 0 or (row, col) in visited:
                        continue

                    dfs(row, col)

        res = 0
        # run for all cels
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0 or (row, col) in visited:
                    continue

                res += dfs(row, col)

        return res


@pytest.mark.parametrize(
    "grid, expected_result",
    (
        (
            [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]],
            3,
        ),
        (
            [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]],
            0,
        ),
        (
            [[1]],
            0,
        ),
    )
)
def test_number_of_enclaves(grid, expected_result):
    assert Solution().numEnclaves(grid) == expected_result
