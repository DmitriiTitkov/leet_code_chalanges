"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard
such that no two queens attack each other. Given an integer n, return all
distinct solutions to the n-queens puzzle. You may return the answer in any
order. Each solution contains a distinct board configuration of the n-queens'
placement, where 'Q' and '.' both indicate a queen and an empty space,
respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown
above

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
1 <= n <= 9
"""
from typing import List

import pytest


class Solution:
    """Backtracking algorithm
    Time: O(n!) each stack frame reduces decision size by one
    Space: O(n*n)
    """
    def is_not_attacked(self, row, col):
        return all((
            (col not in self.cols),
            (row - col not in self.pos_diag),
            (col + row not in self.neg_diag),
        ))

    def place_the_queen(self, row, col, board):
        self.cols.add(col)
        self.pos_diag.add(row - col)
        self.neg_diag.add(col + row)

        board_row = ["."] * len(board)
        board_row[col] = "Q"
        board[row] = "".join(board_row)

    def remove_the_queen(self, row, col, board):
        self.cols.remove(col)
        self.pos_diag.remove(row - col)
        self.neg_diag.remove(col + row)

        board_row = ["."] * len(board)
        board[row] = "".join(board_row)

    def can_place(self, row: int, n: int, board: List, solution: List):
        if row == n:
            solution.append(board[:])

        for col in range(n):
            if self.is_not_attacked(row, col):
                self.place_the_queen(row, col, board)
                self.can_place(row + 1, n, board, solution)
                self.remove_the_queen(row, col, board)

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.cols = set()
        self.pos_diag = set()
        self.neg_diag = set()

        board = [list() for _ in range(n)]
        solution = []
        self.can_place(0, n, board, solution)

        return solution


@pytest.mark.parametrize(
    "n,expected_output", (
        (4, [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]),
        (1, [["Q"]])
    )
)
def test_n_queens(n, expected_output):
    assert Solution().solveNQueens(n) == expected_output
