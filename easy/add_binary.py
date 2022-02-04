"""
https://leetcode.com/problems/add-binary/
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""
from collections import deque
from typing import Tuple

import pytest


def add_bin_numbers(a: str, b: str, carryover: bool) -> Tuple[str, bool]:
    new_carryover = False
    if a == b:
        val = "0"
        if a == "1":
            new_carryover = True
    else:
        val = "1"

    if carryover:
        if val == "1":
            val = "0"
            new_carryover = True
        else:
            val = "1"

    return val, new_carryover


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """Solution without converting strings to integers.
        Time: O(n)
        Space: O(n)
        """

        queue = deque()
        carryover = False

        if len(a) >= len(b):
            long = a
            short = b
        else:
            long = b
            short = a

        for i in range(-1, -len(long) - 1, -1):
            if abs(i) <= len(short):
                val, carryover = add_bin_numbers(long[i], short[i], carryover)
                queue.appendleft(val)
            elif carryover:
                val, carryover = add_bin_numbers(long[i], "0", True)
                queue.appendleft(val)
            else:
                queue.appendleft(long[i])

        if carryover:
            queue.appendleft("1")

        return "".join(queue)




@pytest.mark.parametrize(
    "str1,str2,expected_output",
    (
        ("11", '1', "100"),
        ("1010", "1011", "10101"),

    )
)
def test_combine(str1, str2, expected_output):
    assert Solution().addBinary(str1, str2,) == expected_output