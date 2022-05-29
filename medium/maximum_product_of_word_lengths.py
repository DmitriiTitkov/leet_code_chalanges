"""
Given a string array words, return the maximum value of
length(word[i]) * length(word[j]) where the two words do not share common
letters. If no such two words exist, return 0.

Example 1:
Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".

Example 2:
Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".

Example 3:
Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.

Constraints:
2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] consists only of lowercase English letters.
"""
from typing import List

import pytest


class Solution:
    """
    Compare pairs of letters
    Time: O(c^2)
    Space: O(c)
    c - number of characters
    """
    def maxProduct(self, words: List[str]) -> int:
        words_length = len(words)
        word_maps = [None] * words_length
        max_prod = 0

        for i in range(words_length):
            word_maps[i] = set(words[i])

        for i in range(words_length):
            for j in range(i + 1, words_length):
                for char in words[i]:
                    if char in word_maps[j]:
                        break
                else:
                    max_prod = max(max_prod, len(words[i]) * len(words[j]))

        return max_prod


class Solution2:
    """
    Use bit masks for comparison
    Time: O(n^2)
    Space: O(n)
    n - number of words
    """
    def maxProduct(self, words: List[str]) -> int:
        words_length = len(words)
        masks = [0] * words_length

        for i, word in enumerate(words):
            for char in word:
                masks[i] |= 1 << (ord(char) - ord('a'))

        max_product = 0
        for i in range(words_length):
            for j in range(i + 1, words_length):
                if masks[i] & masks[j] == 0:
                    max_product = max(max_product, len(words[i]) * len(words[j]))

        return max_product


@pytest.mark.parametrize(
    "nums,expected_output", (
        (["abcw","baz","foo","bar", "xtfn", "abcdef"], 16),
        (["a", "ab", "abc", "d", "cd", "bcd", "abcd"], 4),
        (["a", "aa", "aaa", "aaaa"], 0),
    )
)
def test_max_product(nums, expected_output):
    assert Solution().maxProduct(nums) == expected_output
