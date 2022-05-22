"""
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""
import pytest


class Solution:
    """
    Consider each letter as a center of a palindrome, then try to expand to
    find all palindromes.
    Time: O(n**2)
    Space: O(1)
    """
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        palindrome_count = 0

        for i, char in enumerate(s):
            left = right = i
            palindrome_count += 1
            while right < length - 1 and s[right + 1] == char:
                right += 1
                palindrome_count += 1

            while left > 0 and right < length - 1 and s[left - 1] == s[right + 1]:
                right += 1
                left -= 1
                palindrome_count += 1

        return palindrome_count


@pytest.mark.parametrize(
    "s,expected_output",
    (
        ("abc", 3),
        ("aaa", 6),
        ("a", 1),
    )
)
def test_count_substrings(s, expected_output):
    assert Solution().countSubstrings(s) == expected_output
