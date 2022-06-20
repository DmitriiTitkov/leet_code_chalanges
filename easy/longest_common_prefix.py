"""
Write a function to find the longest common prefix string amongst an array of
strings. If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
from typing import List

import pytest


class Solution:
    """
    Time: O(S)
    Space: O(1)

    S = number of characters in all strings
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]

        for word in strs:
            for i in range(max(len(common_prefix), len(word))):
                if i == len(word) or i == len(common_prefix) or word[i] != common_prefix[i]:
                    common_prefix = common_prefix[:i]
                    break

        return common_prefix


@pytest.mark.parametrize(
    "strs,expected_output", (
        (["flower","flow","flight"], "fl"),
        (["dog","racecar","car"], ""),
        (["ab", "a"], "a"),
    )
)
def test_longest_common_prefix(strs, expected_output):
    assert Solution().longestCommonPrefix(strs) == expected_output
