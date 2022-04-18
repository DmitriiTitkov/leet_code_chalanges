"""
There is a robot on an m x n grid. The robot is initially located at the
top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right
corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right
at any point in time.
Given the two integers m and n, return the number of possible unique paths that
the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to
2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:

1 <= m, n <= 100
"""
from functools import lru_cache

import pytest


class Solution:
    """DFS solution with memorization
    Time: O(n)
    Space: O(n)
    """
    def uniquePaths(self, m: int, n: int) -> int:

        @lru_cache
        def dfs(m: int, n: int) -> int:
            res = 0

            if m == 0 and n == 0:
                return 1

            if m > 0:
                res += dfs(m - 1, n)

            if n > 0:
                res += dfs(m, n - 1)

            return res

        return dfs(m - 1, n - 1)


class Solution2:
    """DP approach. Consider each cell as a sum of right and down cells.
    Time: O(N) - where N = m*n  number of cells
    Space: O(min(m,n)) - applied optimization to store minimal amount of cells.

    """
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= n:
            low = m
            high = n
        else:
            low = n
            high = m

        memo = [0] * low
        memo[low - 1] = 1

        for col in range(high - 1, -1, -1):
            prev = 0
            for row in range(low - 1, -1, -1):
                memo[row] = memo[row] + prev
                prev = memo[row]

        return memo[0]


@pytest.mark.parametrize(
    "solution", (Solution, Solution2)
)
@pytest.mark.parametrize(
    "m,n,expected_result",
    (
        (3, 7, 28),
        (3, 2, 3),
    )
)
def test_unique_paths(solution, m, n, expected_result):
    assert solution().uniquePaths(m, n) == expected_result
