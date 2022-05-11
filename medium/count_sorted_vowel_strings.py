"""
Given an integer n, return the number of strings of length n that consist only
of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as
or comes before s[i+1] in the alphabet.

Example 1:
Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

Example 2:
Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

Example 3:
Input: n = 33
Output: 66045

Constraints:
1 <= n <= 50
"""
from functools import cache

import pytest


class Solution:
    """
    Time: O(n*k)
    Space: O(n*k + n) - recursion + cache

    k - amount of vowels - 5
    """
    def countVowelStrings(self, n: int) -> int:

        vowels = ["a", "e", "i", "o", "u"]

        @cache
        def count_vowels_recursive(n, vowel_index) -> int:
            if n == 0:
                return 1

            count = 0

            for i in range(vowel_index, len(vowels)):
                count += count_vowels_recursive( n -1, i)

            return count

        return count_vowels_recursive(n, 0)


@pytest.mark.parametrize(
    "n,expected_output",(
        (1, 5),
        (2, 15),
        (33, 66045),
    )
)
def test_count_vowel_strings(n, expected_output):
    assert Solution().countVowelStrings(n) == expected_output
