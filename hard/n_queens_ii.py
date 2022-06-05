"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard
such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens
puzzle.

Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 9
"""
import pytest


class Solution:
    """
    Backtracking algorithm to count all possible solutions.
    Time: O(n!)
    Space: O(n!)
    """
    def place_queen(self, row: int, col: int) -> None:
        self.cols.add(col)
        self.left_diagonal.add(row-col)
        self.right_diagonal.add(row+col)

    def remove_queen(self, row: int, col: int) -> None:
        self.cols.remove(col)
        self.left_diagonal.remove(row-col)
        self.right_diagonal.remove(row+col)

    def under_attack(self, row: int, col: int) -> bool:
        return (col in self.cols or
                row-col in self.left_diagonal or
                row+col in self.right_diagonal)

    def totalNQueens(self, n: int) -> int:
        self.cols = set()
        self.left_diagonal = set()
        self.right_diagonal = set()

        def get_total_queens(row: int, n: int) -> int:
            if row == n:
                return 1

            total_queens = 0

            for col in range(n):
                if not self.under_attack(row, col):
                    self.place_queen(row, col)
                    total_queens += get_total_queens(row +1, n)
                    self.remove_queen(row, col)

            return total_queens

        return get_total_queens(0, n)


@pytest.mark.parametrize(
    "n,expected_output", (
        (4, 2),
        (2, 0),
        (1, 1),
    )
)
def test_n_queens(n, expected_output):
    assert Solution().totalNQueens(n) == expected_output
