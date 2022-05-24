"""
Given a string containing just the characters '(' and ')', find the length of
the longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0

Constraints:
0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
"""
from typing import List, Union

import pytest


class Solution:
    """
    Use stack to track parentheses and reduce it to number when we find valid
    sequence.
    Time: O(n)
    Space: O(n)
    """
    def reduce(self, stack: List[Union[int, str]], item: int) -> None:
        if item == "(" or len(stack) == 0:
            stack.append(item)
            return

        top = stack[-1]

        if isinstance(item, int):
            if isinstance(top, int):
                top_val = stack.pop()
                self.reduce(stack, top_val + item)
            else:
                stack.append(item)
        else:
            if top == "(":
                stack.pop()
                self.reduce(stack, 2)
            elif isinstance(top, int):
                top = stack.pop()
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                    self.reduce(stack, top + 2)
                else:
                    stack.append(top)
                    stack.append(item)

    def longestValidParentheses(self, s: str) -> int:
        stack = []

        for item in s:
            self.reduce(stack, item)

        max_valied_len = 0
        for item in stack:
            if isinstance(item, int):
                max_valied_len = max(max_valied_len, item)

        return max_valied_len


@pytest.mark.parametrize(
    "s,expected_output",
    (
        ("(()", 2),
        (")()())", 4),
        ("", 0),
    )
)
def test_longest_valid_parentheses(s, expected_output):
    assert Solution().longestValidParentheses(s) == expected_output
