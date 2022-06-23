"""
Given two non-negative integers num1 and num2 represented as strings, return
the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs
to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
Accepted

"""
import pytest


class Solution:
    """
    Use School arithmetic and convert every digit to int. Could use mapping
    instead if requirement is strict.
    Time: O(n * m)
    Space: O(1)

    n - length of the first string
    m - length of the second string
    """
    def multiply_str_by_digit(self, num1: str, num2: str) -> str:
        cur_mul_res = 0
        carry = 0
        for i1, digit1 in enumerate(reversed(num1)):
            res = (int(digit1) * int(num2)) + carry
            cur_mul_res += (res % 10) * 10 ** i1
            carry = res // 10

        cur_mul_res += carry * 10 ** (i1 + 1)
        return cur_mul_res

    def multiply(self, num1: str, num2: str) -> str:
        product = 0

        for i2, digit2 in enumerate(reversed(num2)):
            product += self.multiply_str_by_digit(num1, digit2) * 10 ** i2

        return str(product)


@pytest.mark.parametrize(
    "num1,num2,expexceted_output", (
        ("2", "3", "6"),
        ("123", "456", "56088"),
    )
)
def test_multiply(num1, num2, expexceted_output):
    assert Solution().multiply(num1, num2) == expexceted_output
