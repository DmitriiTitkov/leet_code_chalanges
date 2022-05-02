"""
You are given two m x n binary matrices grid1 and grid2 containing only 0's
(representing water) and 1's (representing land). An island is a group of 1's
connected 4-directionally (horizontal or vertical). Any cells outside of the
grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1
that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.



Example 1:
Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
       grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid
on the right is grid2. The 1s colored red in grid2 are those considered to be
part of a sub-island. There are three sub-islands.

Example 2:
Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],
       grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2
Explanation: In the picture above, the grid on the left is grid1 and the grid
on the right is grid2. The 1s colored red in grid2 are those considered to be
part of a sub-island. There are two sub-islands.

Constraints:
m == grid1.length == grid2.length
n == grid1[i].length == grid2[i].length
1 <= m, n <= 500
grid1[i][j] and grid2[i][j] are either 0 or 1.
"""
from typing import List

import pytest


def is_sub_island(row, col, grid1: List[List[int]], grid2: List[List[int]], visited) -> int:
    stack = [(row, col)]
    res = 1

    while stack:
        row, col = stack.pop()
        visited.add((row,col))

        if grid1[row][col] != 1:
            res = 0

        moves = (row-1, col), (row+1, col), (row, col-1), (row, col+1)

        for r, c in moves:
            if 0 <= r < len(grid2) and 0 <= c < len(grid2[r]):
                if grid2[r][c] == 1 and (r, c) not in visited:
                    stack.append((r, c))

    return res


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        num_sub_islands = 0

        for row in range(len(grid2)):
            for col in range(len(grid2[row])):
                if grid2[row][col] == 0 or (row, col) in visited:
                    continue

                num_sub_islands += is_sub_island(row, col, grid1, grid2, visited)

        return num_sub_islands


@pytest.mark.parametrize(
    "grid1,grid2,expected_output",
    (
        (
            [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]],
            [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]],
            2
        ),
        (
            [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]],
            [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]],
            3
        ),
    )
)
def test_count_sub_islands(grid1, grid2, expected_output):
    assert Solution().countSubIslands(grid1, grid2) == expected_output
