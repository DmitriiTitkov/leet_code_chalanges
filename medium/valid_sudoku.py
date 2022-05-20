"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""
from typing import List


class Solution:
    """
    Traverse 3 times validation rows, columns and squares.
    Time: O(n*n) where n is 9
    Space: O(n)
    """
    def validate_cell(self, board, row, col, numbers):
        if board[row][col] == ".":
            return True
        if board[row][col] in numbers:
            return False
        numbers.add(board[row][col])
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])

        for row in range(rows):
            numbers = set()
            for col in range(cols):
                if not self.validate_cell(board, row, col, numbers):
                    return False

        for col in range(cols):
            numbers = set()
            for row in range(rows):
                if not self.validate_cell(board, row, col, numbers):
                    return False

        for row_group in (0, 3, 6):
            for col_group in (0, 3, 6):
                numbers = set()
                for row in (0, 1, 2):
                    for col in (0, 1, 2):
                        if not self.validate_cell(
                                board,
                                row + row_group,
                                col + col_group,
                                numbers
                        ):
                            return False
        return True
