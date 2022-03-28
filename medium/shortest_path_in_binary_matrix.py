"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/
Given an n x n binary matrix grid, return the length of the shortest clear path
in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0))
to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they
are different and they share an edge or a corner). The length of a clear path
is the number of visited cells of this path.

Example 1:
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1

Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""

from collections import deque
from typing import List

import pytest


class Solution:
    """
    BFS search to find shortest path.
    Time: O(n) where n is number of nodes
    Space: O(n) both queue and stack are linear
    """
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque()
        queue.appendleft((0, 0, 1))

        visited = set()

        while queue:
            row, col, dist = queue.pop()

            if (row, col) in visited or grid[row][col] == 1:
                continue
            visited.add((row, col))

            if row == col == len(grid) - 1:
                return dist

            moves = (
                (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                (row, col - 1), (row, col + 1),
                (row + 1, col - 1), (row + 1, col), (row + 1, col + 1),
            )

            for r, c in moves:
                if 0 <= r < len(grid) and 0 <= c < len(grid):
                    queue.appendleft((r, c, dist + 1))

        return -1


@pytest.mark.parametrize(
    "grid,expected_result",
    (
        ([[0, 1], [1, 0]], 2),
        ([[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4),
        ([[1, 0, 0], [1, 1, 0], [1, 1, 0]], -1),
    )
)
def test_shortest_path(grid, expected_result):
    assert Solution().shortestPathBinaryMatrix(grid) == expected_result
