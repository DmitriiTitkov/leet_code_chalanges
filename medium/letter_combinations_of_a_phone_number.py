"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number
Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given
below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
from typing import List

letter_map = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


class Solution:
    """DFS to find all possible combinations.
    Time: O(4**n * n)
    Space: O(n) For recursive stack. Storing answer takes extra O(4**n)
    """
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []

        def find_comb(digits: List[str], comb: List[str]) -> None:
            if len(digits) == 0:
                res.append("".join(comb))  # O(n)
                return

            # O(n)
            digit = digits[0]
            new_digits = digits[1:] if len(digits) > 1 else ""

            # O(4**n)
            for letter in letter_map[digit]:
                comb.append(letter)
                find_comb(new_digits, comb)
                comb.pop()

        find_comb(digits, [])
        return res
