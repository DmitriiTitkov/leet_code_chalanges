"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
"""
from functools import lru_cache

import pytest


class Solution:
    def climbStairs(self, n: int) -> int:
        """Depth-first search with memorization
        Time: O(n)
        Space: O(n)
        """

        @lru_cache
        def climb(n: int) -> int:
            if n == 0:
                return 1

            res = 0
            if n >= 1:
                res += climb(n-1)

            if n >= 2:
                res += climb(n-2)

            return res

        return climb(n)


@pytest.mark.parametrize(
    "input_num,expected_output",
    (
        (2, 2),
        (3, 3),
        (20, 10946),

    )
)
def test_combine(input_num,expected_output):
    assert Solution().climbStairs(input_num) == expected_output