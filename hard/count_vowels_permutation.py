"""
Given an integer n, your task is to count how many strings of length n can be
formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".

Example 2:
Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu",
"oi", "ou" and "ua".

Example 3:
Input: n = 5
Output: 68

Constraints:
1 <= n <= 2 * 10^4
"""
from functools import cache
from typing import List

import pytest


class Solution:
    """
    Time: O(n * m)
    Space: O(n * m)

    m - number of vowels
    """
    def get_next_chars(self, char: str) -> List[str]:
        char_map = {
            "a": ["e"],
            "e": ["a", "i"],
            "i": ["a", "e", "o", "u"],
            "o": ["i", "u"],
            "u": ["a"]
        }
        return char_map[char]

    def countVowelPermutation(self, n: int) -> int:
        @cache
        def count_perm_recur(i: int, char: str) -> int:
            if i == n - 1:
                return 1

            prem_count = 0
            for next_char in self.get_next_chars(char):
                prem_count += count_perm_recur(i + 1, next_char)

            return prem_count

        return sum(count_perm_recur(0, char) for char in ('a', 'e', 'i', 'o', 'u')) % (10 ** 9 + 7)


@pytest.mark.parametrize(
    "n,expected_output", (
        (1, 5),
        (2, 10),
        (5, 68),
    )
)
def test_count_vowels_permutations(n, expected_output):
    assert Solution().countVowelPermutation(n) == expected_output
