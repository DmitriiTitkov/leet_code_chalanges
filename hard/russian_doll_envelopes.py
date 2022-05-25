"""
You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi]
represents the width and the height of an envelope.
One envelope can fit into another if and only if both the width and height of
one envelope are greater than the other envelope's width and height.
Return the maximum number of envelopes you can Russian doll (i.e., put one
inside the other).
Note: You cannot rotate an envelope.

Example 1:
Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

Example 2:
Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1

Constraints:
1 <= envelopes.length <= 105
envelopes[i].length == 2
1 <= wi, hi <= 105
"""
from typing import List

import pytest


class Solution:
    """
    TODO: Revisit later
    This problem is an extension to longest increasing sequence. With proper
    sorting we can use binary search to overwrite elements in lis array.

    Time: O(n log n)
    Space: O(n)
    """
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        lis = []

        for width, height in envelopes:
            if not lis or lis[-1] < height:
                lis.append(height)
            else:
                l, r = 0, len(lis)

                while l < r:
                    m = (r + l) // 2
                    if lis[m] < height:
                        l = m + 1
                    else:
                        r = m
                lis[l] = height

        return len(lis)


@pytest.mark.parametrize(
    "envelopes,expected_output",
    (
            ([[5, 4], [6, 4], [6, 7], [2, 3]], 3),
            ([[1, 1], [1, 1], [1, 1]], 1),
    )
)
def test_max_envelope(envelopes, expected_output):
    assert Solution().maxEnvelopes(envelopes) == expected_output
