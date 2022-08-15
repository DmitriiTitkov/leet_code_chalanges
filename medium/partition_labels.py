"""
You are given a string s. We want to partition the string into as many parts as
possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in
order, the resultant string should be s.

Return a list of integers representing the size of these parts.



Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]


Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
"""
from typing import List

import pytest


class Solution:
    """
    Greedily expand partition using last index mapping.
    Time: O(n)
    Space: O(1) as we are storing single index for each char. WIth max length 26
    """
    def partitionLabels(self, s: str) -> List[int]:
        latest_index = {v: i for i, v in enumerate(s)}
        res = []
        p_start = p_end = cur = 0

        while p_end < len(s) - 1:
            if cur > p_end:
                res.append(p_end - p_start + 1)
                p_start = cur
                p_end = cur

            if latest_index[s[cur]] > p_end:
                p_end = latest_index[s[cur]]

            cur += 1
        res.append(p_end - p_start + 1)

        return res


@pytest.mark.parametrize(
    "s,expected_output", (
        ("ababcbacadefegdehijhklij", [9, 7, 8]),
        ("eccbbbbdec", [10]),
    )
)
def test_partition_labels(s, expected_output):
    assert Solution().partitionLabels(s) == expected_output
