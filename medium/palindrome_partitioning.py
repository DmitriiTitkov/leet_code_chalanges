"""
Given a string s, partition s such that every substring of the partition is a
palindrome. Return all possible palindrome partitioning of s.
A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.
"""

from functools import cache
from typing import List

import pytest


class Solution:
    def is_palindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    @cache
    def get_palindromes_starting_at(self, s: str, index: int) -> List:
        if index >= len(s):
            return []
        palindromes = []
        for i in range(index, len(s)):
            if self.is_palindrome(s, index, i):
                sub_palindromes = self.get_palindromes_starting_at(s, i + 1)
                if sub_palindromes:
                    for sub_palindrome in self.get_palindromes_starting_at(s, i + 1):
                        palindrome = [s[index:i + 1], *sub_palindrome]
                        palindromes.append(palindrome)
                else:
                    palindrome = [s[index:i + 1]]
                    palindromes.append(palindrome)
        return palindromes

    def partition(self, s: str) -> List[List[str]]:
        return self.get_palindromes_starting_at(s, 0)


@pytest.mark.parametrize(
    "s,expected_output", (
        ("aab", [["a", "a", "b"], ["aa", "b"]]),
        ("a", [["a"]]),
    )
)
def test_partition(s, expected_output):
    assert Solution().partition(s) == expected_output
