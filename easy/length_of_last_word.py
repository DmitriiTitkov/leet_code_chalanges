"""
https://leetcode.com/problems/length-of-last-word/
Given a string s consisting of some words separated by some number of spaces,
return the length of the last word in the string. A word is a maximal substring
consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:
1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""
import pytest


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """Two pointer solution
        Time: O(n)
        Space: O(1)
        """
        curr = prev_curr = 0
        word_length = 0

        while curr < len(s):
            if s[curr] != ' ':
                if s[prev_curr] == ' ':
                    word_length = 1
                else:
                    word_length += 1

            prev_curr = curr
            curr += 1

        return word_length


@pytest.mark.parametrize(
    "s,expected_output",
    (
        ("test test test", 4),
        ("test test t", 1),
        ("bla", 3),
        ("bla   ", 3),
        ("bla   asd   ", 3),

    )
)
def test_combine(s, expected_output):
    assert Solution().lengthOfLastWord(s) == expected_output
