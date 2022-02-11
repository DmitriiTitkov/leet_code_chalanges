"""
https://leetcode.com/problems/power-of-two/
Given an integer n, return true if it is a power of two. Otherwise, return
false. An integer n is a power of two, if there exists an integer x such that n
== 2x.

Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:
Input: n = 3
Output: false

Constraints:
-231 <= n <= 231 - 1
"""
import pytest


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Time: O(1)
        Space: O(1)

        n and n -1 will always cancel each other if n is a power of 2. Ex:
        (1000 & 0111) == 0
        """
        return n > 0 and n & (n-1) == 0


@pytest.mark.parametrize(
    "num,expected_output",
    (
        (0, False),
        (1, True),
        (2, True),
        (3, False),
        (128, True),
    )
)
def test_is_power_of_two(num, expected_output):
    assert Solution().isPowerOfTwo(num) == expected_output
