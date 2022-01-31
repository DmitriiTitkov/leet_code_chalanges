"""
https://leetcode.com/problems/longest-palindromic-substring/
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""
import pytest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Calculate all palindromes starting from the center of substring.
        Time: O(n^2). Worst case input example: 'abababababababa'
        Space: O(1)
        """
        def get_palindrome(l: int, r: int):
            while l >= 1 and r < len(s) -1:
                if s[l-1] == s[r+1]:
                    l -= 1
                    r += 1
                else:
                    return s[l:r+1]

            return s[l:r+1]

        r = l = 0
        max_pal = ''

        # O(n)
        while r < len(s):
            if r < len(s) -1 and s[r] == s[r+1]:
                r += 1
                continue
            else:
                max_pal = max(get_palindrome(l, r), max_pal, key=len)
                r+=1
                l = r

        return max_pal


@pytest.mark.parametrize(
    "s,expected_output",
    (
        ("aba", "aba"),
        ("babad", "aba"),
        ("cbbd", "bb"),
    )
)
def test_combine(s, expected_output):
    assert Solution().longestPalindrome(s) == expected_output
