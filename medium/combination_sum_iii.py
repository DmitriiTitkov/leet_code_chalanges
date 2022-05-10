"""
Find all valid combinations of k numbers that sum up to n such that the
following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the
same combination twice, and the combinations may be returned in any order.

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is
1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

Constraints:
2 <= k <= 9
1 <= n <= 60
"""
from typing import List

import pytest


class Solution:
    """
    Time: O(2**k * k)
    Space: O(k)
    """
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        combinations = []

        def combine(index, comb, cur_sum):
            cur_sum += options[index]
            comb.append(options[index])

            if cur_sum > n:
                comb.pop()
                return

            if len(comb) == k:
                if cur_sum == n:
                    combinations.append(comb[:])
                comb.pop()
                return

            for i in range(index+1, 9):
                combine(i, comb, cur_sum)

            comb.pop()

        for i in range(len(options)):
            combine(i, [], 0)
        return combinations


@pytest.mark.parametrize(
    "k,n,expected_output",
    (
        (3, 7, [[1,2,4]]),
        (3, 9, [[1,2,6],[1,3,5],[2,3,4]]),
        (4, 1, []),

    )
)
def test_combination_sum(k, n, expected_output):
    assert Solution().combinationSum3(k, n) == expected_output
