"""
You are given an m x n matrix maze (0-indexed) with empty cells
(represented as '.') and walls (represented as '+'). You are also given the
entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the
row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step
into a cell with a wall, and you cannot step outside the maze. Your goal is to
find the nearest exit from the entrance. An exit is defined as an empty cell
that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the
nearest exit, or -1 if no such path exists.

Example 1:
Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.

Example 2:
Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.

Example 3:
Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.


Constraints:
maze.length == m
maze[i].length == n
1 <= m, n <= 100
maze[i][j] is either '.' or '+'.
entrance.length == 2
0 <= entrancerow < m
0 <= entrancecol < n
entrance will always be an empty cell.
"""
from collections import deque
from typing import List

import pytest


class Solution:
    """Use BFS to traverse through maze and store path length in visited maze
    cells.
    Time: O(m*n)
    Space: O(m*n) - actual will be much less
    """
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row_count = len(maze)
        col_count = len(maze[0])

        e_row, e_col = entrance[0], entrance[1]
        maze[e_row][e_col] = 0

        queue = deque()
        queue.appendleft((e_row, e_col))

        while queue:
            row, col = queue.pop()

            if (maze[row][col] != 0 and
                    (row in (0, row_count - 1) or col in (0, col_count - 1))
            ):
                return maze[row][col]

            moves = (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)

            for r, c in moves:
                if 0 <= r < row_count and 0 <= c < col_count and maze[r][c] == ".":
                    maze[r][c] = maze[row][col] + 1
                    queue.appendleft((r, c))

        return -1


@pytest.mark.parametrize(
    "maze,entrance,expected_output",
    (
        ([["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2], 1),
        ([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0], 2),
        ([[".", "+"]], [0, 0], -1),
    )
)
def test_nearest_exit(maze, entrance, expected_output):
    assert Solution().nearestExit(maze, entrance) == expected_output
