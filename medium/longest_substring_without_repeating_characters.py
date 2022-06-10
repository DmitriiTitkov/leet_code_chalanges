"""
Given a string s, find the length of the longest substring without repeating
characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a
substring.


Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
import pytest


class Solution:
    """
    Sliding window approach
    Time: O(n)
    Space: O(n)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        cur_substr = set()
        max_substr_len = 0

        while r < len(s):
            if s[r] not in cur_substr:
                cur_substr.add(s[r])
                r += 1
            else:
                cur_substr.remove(s[l])
                l += 1

            max_substr_len = max(max_substr_len, len(cur_substr))

        return max_substr_len


@pytest.mark.parametrize(
    "input_str,expected_result",
    (
            ("abcabcbb", 3),
            ("bbbbbbb", 1),
            ("pwwkew", 3),
            ("a", 1),
            ("", 0),

    )
)
def test_search(input_str, expected_result):
    assert Solution().lengthOfLongestSubstring(input_str) == expected_result
