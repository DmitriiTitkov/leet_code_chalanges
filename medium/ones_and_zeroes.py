"""
https://leetcode.com/problems/ones-and-zeroes/
You are given an array of binary strings strs and two integers m and n.
Return the size of the largest subset of strs such that there are at most m 0's
and n 1's in the subset. A set x is a subset of a set y if all elements of x
are also elements of y.

Example 1:
Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

Example 2:
Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.

Constraints:
1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100
"""
from functools import cache
from typing import List

import pytest


class Solution:
    """
    TODO: Solve similar task
    Time: (L * m * n)
    Space: (L * m * n)
    """
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = [0] * len(strs)

        for i, s in enumerate(strs):
            zero_count = 0
            one_count = 0
            for bin_char in s:
                if bin_char == '0':
                    zero_count +=1
                else:
                    one_count +=1
            counts[i] = (zero_count, one_count)

        @cache
        def find_max_subset_length(index, m, n):
            if index == len(strs) or m + n == 0:
                return 0

            max_subset = 0

            if counts[index][0] <= m and counts[index][1] <= n:
                max_subset = 1 + find_max_subset_length(
                    index +1, m-counts[index][0],
                    n-counts[index][1]
                )

            max_subset = max(max_subset, find_max_subset_length(index+1, m, n))
            return max_subset

        return find_max_subset_length(0, m, n)


@pytest.mark.parametrize(
    "strs,m,n,expected_output",
    (
        (["10","0001","111001","1","0"], 5, 3, 4),
        (["10","0","1"], 1, 1, 2),
    )
)
def test_find_max_from(strs, m, n, expected_output):
    assert Solution().findMaxForm(strs, m, n) == expected_output
