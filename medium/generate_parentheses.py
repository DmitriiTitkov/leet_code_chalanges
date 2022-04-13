"""
https://leetcode.com/problems/generate-parentheses/
Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
"""
from typing import List

import pytest


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_br: int, close_br: int, comb: List[str]):
            if open_br == 0 and close_br == 0:
                res.append("".join(comb))
                return

            if open_br > 0:
                comb.append("(")
                backtrack(open_br - 1, close_br + 1, comb)
                comb.pop()

            if close_br > 0:
                comb.append(")")
                backtrack(open_br, close_br - 1, comb)
                comb.pop()

        backtrack(n, 0, [])
        return res


@pytest.mark.parametrize(
    "n,expected_result",
    (
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        (1, ["()"])
    )
)
def test_generate_parentheses(n, expected_result):
    assert Solution().generateParenthesis(n) == expected_result
