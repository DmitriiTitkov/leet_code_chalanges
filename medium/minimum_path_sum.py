"""
Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
"""
from typing import List

import pytest


class Solution:
    """
    DP approach use left bottom as base case and calculate min value using
    right and bottom cells.
    Time: O(n * m) - number of cells
    Space: O(1)
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        for row in range(len(grid) - 1, -1, -1):
            for col in range(len(grid[0]) - 1, -1, -1):
                min_val = float("inf")

                if row < len(grid) - 1:
                    min_val = grid[row + 1][col]

                if col < len(grid[0]) - 1:
                    min_val = min(min_val, grid[row][col + 1])

                if min_val != float("inf"):
                    grid[row][col] = min_val + grid[row][col]
                else:
                    grid[row][col] = grid[row][col]

        return grid[0][0]


@pytest.mark.parametrize(
    "grid,expected_output", (
        ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),
        ([[1, 2, 3], [4, 5, 6]], 12,),
    )
)
def test_min_path_sum(grid, expected_output):
    assert Solution().minPathSum(grid) == expected_output
