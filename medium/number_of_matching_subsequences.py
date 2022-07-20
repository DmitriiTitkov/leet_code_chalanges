"""
Given a string s and an array of strings words, return the number of words[i]
that is a subsequence of s.

A subsequence of a string is a new string generated from the original string
with some characters (can be none) deleted without changing the relative order
of the remaining characters.

For example, "ace" is a subsequence of "abcde".

Example 1:
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a",
"acd", "ace".

Example 2:
Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2


Constraints:

1 <= s.length <= 5 * 104
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.
"""
from bisect import bisect_right
from typing import List

import pytest


class Solution:
    """
    Store indexes and use binary search to find next index for a letter.
    Time: O(n log n)
    Space: O(k)
    k - length of string s
    n - total amount of letters in words
    """
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        indexes = [[] for _ in range(26)]

        for i, letter in enumerate(s):
            indexes[ord(letter) - ord('a')].append(i)

        subsequence_count = 0

        for word in words:
            prev_index = -1
            for letter in word:
                letter_indexes = indexes[ord(letter) - ord('a')]
                if not letter_indexes:
                    break

                i = bisect_right(letter_indexes, prev_index)
                if i == len(letter_indexes):
                    break
                prev_index = letter_indexes[i]
            else:
                subsequence_count += 1

        return subsequence_count


@pytest.mark.parametrize(
    "s,words,expected_output", (
        ("abcde", ["a", "bb", "acd", "ace"], 3),
        ("dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"], 2),
    )
)
def test_num_matching_subsec(s,words,expected_output):
    assert Solution().numMatchingSubseq(s, words) == expected_output
