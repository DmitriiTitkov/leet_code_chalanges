"""
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal
4-directionally connected group of 0s and a closed island is an island totally
(all left, top, right, bottom) surrounded by 1s.
Return the number of closed islands.

Example 1:
Input: grid = [[1,1,1,1,1,1,1,0],
               [1,0,0,0,0,1,1,0],
               [1,0,1,0,1,1,1,0],
               [1,0,0,0,0,1,0,1],
               [1,1,1,1,1,1,1,0]]
Output: 2
Explanation:
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:
Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Example 3:
Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2

Constraints:
1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
"""
from collections import deque
from typing import List

import pytest


class Solution:
    """
    BFS Traverse grid on edges and in center separately. Mark traversed as
    visited and increase counter when encountering island in the middle of the
    grid.
    Time: O(N) every cell visited once
    Space: O(2N) queue and visited set
    """
    def bfs(self, grid, row, col, visited):
        queue = deque()
        queue.appendleft((row, col))

        while queue:
            row, col = queue.pop()
            visited.add((row, col))

            moves = (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)

            for r, c in moves:
                if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
                    if (r, c) in visited or grid[r][c] == 1:
                        continue

                    queue.appendleft((r, c))

    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        res = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if (row, col) in visited:
                    continue

                if row in (0, len(grid) - 1) or col in (0, len(grid[row]) - 1):
                    if grid[row][col] == 0:
                        self.bfs(grid, row, col, visited)

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if (row, col) in visited:
                    continue

                if grid[row][col] == 0:
                    res += 1
                    self.bfs(grid, row, col, visited)

        return res


@pytest.mark.parametrize(
    "grid,expected_output",
    (
        (
            [[1, 1, 1, 1, 1, 1, 1, 0],
             [1, 0, 0, 0, 0, 1, 1, 0],
             [1, 0, 1, 0, 1, 1, 1, 0],
             [1, 0, 0, 0, 0, 1, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 0]],

            2
        ),
        (
            [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]],
            1
        ),
    )
)
def test_closed_island(grid, expected_output):
    assert Solution().closedIsland(grid) == expected_output
