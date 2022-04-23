"""
Given a string s and a dictionary of strings wordDict, return true if s can be
segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the
segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen
apple". Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""
from functools import lru_cache
from typing import List

import pytest


class Solution:
    """DFS Solution
    Time: O(n) - as the word limited to 20 characters and doesn't grow with
          input.
    Space: O(n) - worst case complexity for memorization
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        w_dict = set(wordDict)

        @lru_cache
        def dfs(start: int) -> bool:
            res = False
            for end in range(start, min(len(s) + 1, start + 20)):
                substr = s[start:end]

                if substr in w_dict:
                    if end == len(s):
                        return True
                    res = dfs(end)
                    if res is True:
                        return True

            return res

        return dfs(0)


@pytest.mark.parametrize(
    "s,word_dict,expected_result",
    (
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    )
)
def test_word_break(s, word_dict, expected_result):
    assert Solution().wordBreak(s, word_dict) == expected_result
