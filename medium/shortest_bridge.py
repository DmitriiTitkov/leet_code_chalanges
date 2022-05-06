"""
You are given an n x n binary matrix grid where 1 represents land and 0
represents water. An island is a 4-directionally connected group of 1's not
connected to any other 1's. There are exactly two islands in grid.
You may change 0's to 1's to connect the two islands to form one island.
Return the smallest number of 0's you must flip to connect the two islands.

Example 1:
Input: grid = [[0,1],[1,0]]
Output: 1

Example 2:
Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:
Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

Constraints:
n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
"""
from collections import deque
from typing import List

import pytest


class Solution:
    """Use DFS to flip first island and DFS to reach to second
    Time: O(n)
    Space: O(n)
    n - number of cells
    """
    def shortestBridge(self, grid: List[List[int]]) -> int:
        length = len(grid)

        def find_edges(row, col, borders):
            grid[row][col] = 2

            moves = (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)
            for r, c in moves:
                if 0 <= r < length and 0 <= c < length and grid[r][c] != 2:
                    if grid[r][c] == 1:
                        find_edges(r, c, borders)
                    else:
                        borders.appendleft((row, col))

        def bfs(queue) -> int:

            while queue:
                row, col = queue.pop()
                cur_dist = grid[row][col]

                moves = (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)
                for r, c in moves:
                    if 0 <= r < length and 0 <= c < length:
                        if grid[r][c] == 0:
                            grid[r][c] = cur_dist + 1
                            queue.appendleft((r, c))

                        if grid[r][c] == 1:
                            return grid[row][col] - 2

        queue = deque()
        first_island = None

        row = col = 0
        while not first_island:
            if grid[row][col] == 1:
                first_island = (row, col)
                break

            if col < length - 1:
                col += 1
            else:
                col = 0
                row += 1

        find_edges(first_island[0], first_island[1], queue)
        return bfs(queue)


@pytest.mark.parametrize(
    "grid,expected_result",
    (
        ([[0, 1], [1, 0]], 1),
        ([[0, 1, 0], [0, 0, 0], [0, 0, 1]], 2),
        (
            [
                [1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1]
            ],
            1
        ),
    )
)
def test_shortest_path(grid, expected_result):
    assert Solution().shortestBridge(grid) == expected_result
