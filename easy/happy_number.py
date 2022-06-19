"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the
squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops
endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false

Constraints:
1 <= n <= 231 - 1
"""
import pytest


class Solution:
    """
    Detect cycle by using set.
    Time: O(logn) - number shrinks eventually as every digit gives two digit
    square at max.
    Space: O(1) - there will be constant number of nums(243) that is stored in
    set
    """
    def isHappy(self, n: int) -> bool:
        checked = set()

        cur_sum = 0
        while True:
            while n:
                digit = n % 10
                n //= 10
                cur_sum += digit * digit

            if cur_sum in checked:
                return False
            if cur_sum == 1:
                return True

            if cur_sum < 300:
                checked.add(cur_sum)
            n = cur_sum
            cur_sum = 0


@pytest.mark.parametrize(
    "n,expected_output", (
        (19, True),
        (2, False),
    )
)
def test_happy_number(n, expected_output):
    assert Solution().isHappy(n) == expected_output
