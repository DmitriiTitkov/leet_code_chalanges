"""
Given an array of strings strs, group the anagrams together. You can return the
answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from collections import defaultdict
from typing import List

import pytest


class Solution:
    """Use sorted word as for gouping

    Time: O(n * k logk)
    Space: O(n * k)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            anagrams[sorted_word].append(word)

        return [v for v in anagrams.values()]


class Solution2:
    """
    Use character count for grouping
    Time: O(n * k)
    Space: O (n * k)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            char_count = [0] * 26
            shift = ord('a')

            for char in word:
                char_count[ord(char) - shift] += 1

            char_count = tuple(char_count)
            anagrams[char_count].append(word)

        return [v for v in anagrams.values()]



@pytest.mark.parametrize(
    "strs,expected_output",
    (
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
        (
            [""], [[""]],
        ),
        (
            ["a"], [["a"]],
        ),
    )
)
def test_group_anagrams(strs, expected_output):
    assert Solution().groupAnagrams(strs) == expected_output
