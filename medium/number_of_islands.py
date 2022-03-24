"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and
'0's (water), return the number of islands. An island is surrounded by water
and is formed by connecting adjacent lands horizontally or vertically. You may
assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
from typing import List

import pytest
from _collections import deque


class Solution:
    """DFS with memorization. Use set to remember all visited cells.
    Time: O(n)
    Space: O(n) linear time complexity for visited set and for recursion stack
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        island_count = 0

        def is_island(row: int, col: int) -> int:
            if (row, col) in visited or grid[row][col] == "0":
                return 0

            visited.add((row, col))

            neighbors = (row, col-1), (row, col+1), (row-1, col), (row+1, col)

            # mark visited
            for r, c in neighbors:
                if 0 <= r < len(grid) and 0 <= c < len(grid[row]):
                    if grid[r][c] == "1":
                        is_island(r, c)
            return 1

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                island_count += is_island(row, col)

        return island_count


class Solution2:
    """DFS with input data mutation.
    Time: O(n)
    Space: O(n) Worst case linear time complexity for recursion stack.
    """
    def numIslands(self, grid: List[List[str]]) -> int:

        island_count = 0

        def is_island(row: int, col: int) -> int:
            if grid[row][col] == "0":
                return 0

            grid[row][col] = "0"

            neighbors = (row, col-1), (row, col+1), (row-1, col), (row+1, col)

            # mark visited
            for r, c in neighbors:
                if 0 <= r < len(grid) and 0 <= c < len(grid[row]):
                    if grid[r][c] == "1":
                        is_island(r, c)
            return 1

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                island_count += is_island(row, col)

        return island_count


@pytest.mark.parametrize(
    "solution", (Solution, Solution2)
)
@pytest.mark.parametrize(
    "grid,expected_result",
    (
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]
            ],
            1
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"]
            ],
            3
        ),

    )
)
def test_island_count(solution, grid, expected_result):
    assert solution().numIslands(grid) == expected_result
