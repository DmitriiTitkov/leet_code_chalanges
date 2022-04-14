"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring. The same letter cell
may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
"""

from typing import List

import pytest


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(row: int, col: int, letter_i: int, used_cells) -> bool:
            if board[row][col] != word[letter_i] or (row, col) in used_cells:
                return False
            used_cells.add((row, col))

            if len(word) - 1 == letter_i:
                return True

            for r, c in (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1):
                if not (0 <= r < len(board) and 0 <= c < len(board[row])):
                    continue

                if dfs(r, c, letter_i + 1, used_cells):
                    return True

            used_cells.remove((row, col))
            return False

        # (M * N * 3) ** C
        for row in range(len(board)):
            for col in range(len(board[row])):
                if dfs(row, col, 0, set()):
                    return True

        return False



@pytest.mark.parametrize(
    "board,word,expected_result",
    (
        (
            [
                ["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]
            ],
            "ABCCED",
            True,
        ),
        (
            [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "SEE",
            True,
        ),
        (
            [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "ABCB",
            False,
        ),
    )
)
def test_word_search(board, word, expected_result):
    assert Solution().exist(board, word) == expected_result
