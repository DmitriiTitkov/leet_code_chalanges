"""
You are given two strings of the same length s and t. In one step you can
choose any character of t and replace it with another character.
Return the minimum number of steps to make t an anagram of s.
An Anagram of a string is a string that contains the same characters with a
different (or the same) ordering.

Example 1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

Example 2:
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters
to make t anagram of s.

Example 3:
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams.

Constraints:
1 <= s.length <= 5 * 104
s.length == t.length
s and t consist of lowercase English letters only.
"""
from collections import Counter

import pytest


class Solution:
    """Count letters that don't match
    Time: O(n)
    Space: O(1) - as we store maximum 26 chars
    """
    def minSteps(self, s: str, t: str) -> int:
        counts = Counter(s)
        ops = 0
        for char in t:
            if char in counts and counts[char] > 0:
                counts[char] -= 1
            else:
                ops += 1

        return ops


@pytest.mark.parametrize(
    "s,t,expected_output", (
            ("bab", "aba", 1),
            ("leetcode", "practice", 5),
            ("leetcode", "practice", 5),
            ("anagram", "mangaar", 0),
    )
)
def test_min_steps(s, t, expected_output):
    assert Solution().minSteps(s, t) == expected_output
