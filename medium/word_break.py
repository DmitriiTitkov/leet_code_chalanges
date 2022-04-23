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
          input. O(n) is very arguable as limiting factor doesn't work for short
          strings, and the constant is still quite big.

          Considering that min(lenght, 20) works as a constant:
          m + n * 20 * 20

          Considering lsn(s) < 20:
          m + n * n * n

    Space: O(n+m) - worst case complexity for memorization abd set
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # o(m) - m - length of wordDict
        w_dict = set(wordDict)

        @lru_cache
        def dfs(start: int) -> bool:
            res = False
            # loop of max 20
            for end in range(start, min(len(s) + 1, start + 20)):
                # slice of max 20
                substr = s[start:end]

                # o(1) inclusion check
                if substr in w_dict:
                    if end == len(s):
                        return True
                    res = dfs(end)
                    if res is True:
                        return True

            return res

        return dfs(0)


class Solution2:
    """
    DP Solution
    Time complexity is similar to DFS solution and depends on weather to accept
    min(20,n) as a constant.

    Time: O(m + n + n * min(20,n) * min(20,n))
    Space: O(n+m)
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # n
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        # m
        word_set = set(wordDict)

        # n
        for start in range(len(s), -1, -1):
            # min(20, n)
            for stop in range(start, min(len(s), start+20)):
                # slice min(20, n)
                if s[start:stop+1] in word_set and dp[stop+1]:
                    dp[start] = True
                    break

        return dp[0]


@pytest.mark.parametrize(
    "solution", [Solution, Solution2]
)
@pytest.mark.parametrize(
    "s,word_dict,expected_result",
    (
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    )
)
def test_word_break(solution, s, word_dict, expected_result):
    assert Solution().wordBreak(s, word_dict) == expected_result
