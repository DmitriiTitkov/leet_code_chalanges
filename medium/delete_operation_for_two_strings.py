"""
Given two strings word1 and word2, return the minimum number of steps required
to make word1 and word2 the same.
In one step, you can delete exactly one character in either string.

Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make
"eat" to "ea".

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4

Constraints:
1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.
"""
from functools import cache

import pytest


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @cache
        def common_subseq(w1_index, w2_index) -> int:
            if w1_index == len(word1) or w2_index == len(word2):
                return 0

            if word1[w1_index] == word2[w2_index]:
                return 1 + common_subseq(w1_index+1, w2_index+1)

            return max(
                common_subseq(w1_index+1, w2_index),
                common_subseq(w1_index, w2_index+1),
            )

        return len(word1) + len(word2) - 2 * common_subseq(0, 0)


@pytest.mark.parametrize(
    "word1,word2,expected_output", (
        ("sea", "eat", 2),
        ("leetcode", "etco", 4),
    )
)
def test_min_distance(word1, word2, expected_output):
    assert Solution().minDistance(word1, word2), expected_output
