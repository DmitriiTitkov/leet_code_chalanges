"""
You are given an array of strings words. Each element of words consists of two
lowercase English letters.

Create the longest possible palindrome by selecting some elements from words
and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is
impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.
Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt",
of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".


Constraints:

1 <= words.length <= 105
words[i].length == 2
words[i] consists of lowercase English letters.
"""
from collections import Counter
from typing import List

import pytest


class Solution:
    """
    Use two counters to count reversed words, and append counts to length of
    palindrome. One word can be injected in the middle if it has identical letters.
    Time: O(n)
    Space: O(n)
    n - number of characters
    """
    def longestPalindrome(self, words: List[str]) -> int:
        reversed_words = Counter()
        double_letters = Counter()

        for word in words:
            word_rev = word[::-1]
            if word_rev == word:
                double_letters[word] += 1
            else:
                reversed_words[word_rev] += 1

        total_palindrom_length = 0
        inject_in_middle = False

        for word in words:
            if reversed_words[word] > 0:
                total_palindrom_length += 2
                reversed_words[word] -= 1

        for word, count in double_letters.items():
            if count >= 2:
                total_palindrom_length += (count - count % 2) * 2
                count %= 2

            if count == 1:
                inject_in_middle = True

        return total_palindrom_length if not inject_in_middle else total_palindrom_length + 2


@pytest.mark.parametrize(
    "words,expected_output", (
        (["lc", "cl", "gg"], 6),
        (["ab", "ty", "yt", "lc", "cl", "ab"], 8),
        (["cc", "ll", "xx"], 2),
    )
)
def test_longest_palindrome(words, expected_output):
    assert Solution().longestPalindrome(words) == expected_output
