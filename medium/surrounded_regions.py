"""
https://leetcode.com/problems/surrounded-regions/
Given an m x n matrix board containing 'X' and 'O', capture all regions that
are 4-directionally surrounded by 'X'. A region is captured by flipping all
'O's into 'X's in that surrounded region.

Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Example 2:
Input: board = [["X"]]
Output: [["X"]]

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""
from typing import List

import pytest


class Solution:
    """
    Traverse all edges and use DFS to flip all adjusting letters to something
    temporary. Then flip all O to X, and reverse temporary vals to O.
    Time: O(n * m) - traverse all elements twice
    Space: O(n * m) - worst case recursion
    """
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def capture(row, col, new_letter):
            board[row][col] = new_letter

            moves = (row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)

            for r, c in moves:
                if 0 <= r < len(board) and 0 <= c < len(board[r]):
                    if board[r][c] == "O":
                        capture(r, c, new_letter)

        for row in range(len(board)):
            for col in range(len(board[row])):
                if 1 <= row < len(board) - 1 and 1 <= col < len(board[row]) - 1:
                    continue
                if board[row][col] == "O":
                    capture(row, col, "E")

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == "E":
                    board[row][col] = "O"
                else:
                    board[row][col] = "X"


@pytest.mark.parametrize(
    "grid,expected_result",
    (
        (
            [
                ["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"],
            ],
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "O", "X", "X"],
            ]
        ),
        (
            [["X"]], [["X"]]
        ),
    )
)
def test_solve(grid, expected_result):
    Solution().solve(grid)
    assert grid == expected_result
