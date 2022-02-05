"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range
[-2**31, 2**31 - 1], then return 0. Assume the environment does not allow you
to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Constraints:
-231 <= x <= 231 - 1
"""
import pytest


class Solution:
    def reverse(self, x: int) -> int:
        divider = 10
        accum = 0
        res = []
        positive = True

        if -10 < x < 10:
            return x

        if x < 0:
            positive = False

        x = abs(x)

        while True:
            digit = x % divider - accum
            res.append(digit // (divider // 10))

            if x % divider == x:
                break

            divider *= 10
            accum += digit

        res2= 0
        for i, num in enumerate(res):
            res2 += num * 10 ** (len(res) -1 - i)

        res2 = res2 if positive else -res2
        if abs(res) >= 2**31:
            return 0

        return res2


@pytest.mark.parametrize(
    "input_num,expected_output",
    (
        (123, 321),

    )
)
def test_combine(input_num,expected_output):
    assert Solution().reverse(input_num) == expected_output