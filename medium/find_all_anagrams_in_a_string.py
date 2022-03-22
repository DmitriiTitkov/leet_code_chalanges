"""
Given two strings s and p, return an array of all the start indices of p's
anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:
1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""
from collections import Counter
from typing import List

import pytest


class Solution:
    """Use lowercase alphabet counts to compare if anagram is found.
    Time: O(n) Iterate over string only once. 26 comparisons are done on each
    letter, but this number is a constant.

    Space O(n) Space is used to store final answer which at max can be equals to
    length of haystack.
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        needle_char_count = [0] * 26
        haystack_char_count = [0] * 26
        left = 0
        right = len(p) - 1
        res = []

        for char in p:
            index = ord(char) - 97
            needle_char_count[index] += 1

        for char in s[0:len(p)]:
            index = ord(char) - 97
            haystack_char_count[index] += 1

        while right < len(s):
            if needle_char_count == haystack_char_count:
                res.append(left)

            if right == len(s) - 1:
                break

            right += 1
            haystack_char_count[ord(s[right]) - 97] += 1

            haystack_char_count[ord(s[left]) - 97] -= 1
            left += 1

        return res


class Solution2:
    """Use Counter to store counts of letter in needle an haystack
    Time: O(n)
    Space O(n) Space is used to store final answer which at max can be equals to
    length of haystack.
    """

    def findAnagrams(self, s: str, p: str) -> List[int]:
        needle_char_count = Counter(p)
        haystack_char_count = Counter(s[0:len(p)])
        left = 0
        right = len(p) - 1
        res = []

        while right < len(s):
            if needle_char_count == haystack_char_count:
                res.append(left)

            if right == len(s) - 1:
                break

            right += 1
            haystack_char_count[s[right]] += 1

            haystack_char_count[s[left]] -= 1
            left += 1

        return res


@pytest.mark.parametrize(
    "solution", (Solution, Solution2)
)
@pytest.mark.parametrize(
    "s,p,expected_output",
    (
        ("cbaebabacd", "abc", [0, 6]),
        ("abab", "ab", [0, 1, 2]),
    )
)
def test_find_anagrams(solution, s, p, expected_output):
    assert solution().findAnagrams(s, p) == expected_output
