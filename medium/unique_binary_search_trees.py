"""
Given an integer n, return the number of structurally unique BST's
(binary search trees) which has exactly n nodes of unique values from 1 to n.

Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 19
"""
from functools import cache

import pytest


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """
    def numTrees(self, n: int) -> int:

        @cache
        def num_trees_rec(n: int) -> int:
            if n <= 1:
                return 1

            total_configurations = 0
            for i in range(1, n + 1):
                total_configurations += num_trees_rec(i - 1) * num_trees_rec(n - i)

            return total_configurations

        return num_trees_rec(n)


@pytest.mark.parametrize(
    "n,expected_result", (
        (1, 1),
        (3, 5),
    )
)
def test_num_trees(n, expected_result):
    assert Solution().numTrees(n) == expected_result
