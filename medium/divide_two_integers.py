"""
Given two integers dividend and divisor, divide two integers without using
multiplication, division, and mod operator.
The integer division should truncate toward zero, which means losing its
fractional part. For example, 8.345 would be truncated to 8, and -2.7335
would be truncated to -2.

Return the quotient after dividing dividend by divisor. Note: Assume we are
dealing with an environment that could only store integers within the 32-bit
signed integer range: [−231, 231 − 1]. For this problem, if the quotient is
strictly greater than 231 - 1, then return 231 - 1, and if the quotient is
strictly less than -231, then return -231.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Constraints:
-231 <= dividend, divisor <= 231 - 1
divisor != 0
"""
import pytest

MAX_INT = 2147483647
MIN_INT = -2147483648


class Solution:
    """
    Use bitshift operator to double the value until it reaches dividend. Then
    repeat for remainder.

    Time: O(log n)
    Space: O(1)
    n - value of dividend
    """
    def divide(self, dividend: int, divisor: int) -> int:
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)

        remainder = dividend_abs
        ans = 0

        while remainder >= divisor_abs:
            if remainder == divisor_abs:
                ans += 1
                break

            cur_found_remainder = divisor_abs
            quotient = 1

            while cur_found_remainder < remainder:
                cur_found_remainder <<= 1
                quotient <<= 1

            remainder -= cur_found_remainder >> 1
            ans += quotient >> 1

        signed_ans = -ans if (dividend > 0) ^ (divisor > 0) else ans
        if signed_ans > MAX_INT:
            return MAX_INT
        elif signed_ans < MIN_INT:
            return MIN_INT

        return signed_ans


@pytest.mark.parametrize(
    "dividend,divisor,expected_output",
    (
        (10, 3, 3),
        (7, -3, -2),
        (1, 1, 1)
    )
)
def test_divide_two_integers(dividend, divisor, expected_output):
    assert Solution().divide(dividend, divisor) == expected_output
