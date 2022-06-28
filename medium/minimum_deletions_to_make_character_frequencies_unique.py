"""
A string s is called good if there are no two different characters in s that
have the same frequency. Given a string s, return the minimum number of
characters you need to delete to make s good. The frequency of a character in a
string is the number of times it appears in the string. For example, in the
string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Example 1:
Input: s = "aab"
Output: 0
Explanation: s is already good.

Example 2:
Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

Example 3:
Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end
(i.e. frequency of 0 is ignored).

Constraints:

1 <= s.length <= 105
s contains only lowercase English letters.
"""
from collections import Counter

import pytest


class Solution:
    """
    Decrement counts of unique numbers.
    Time: O(n + k^2)
    Space: O(k)

    n - length of s
    k - number of unique characters in s
    """
    def minDeletions(self, s: str) -> int:
        counts = Counter(s)
        unique_counts = set()
        ops = 0

        for cnt in counts.values():
            while cnt > 0 and cnt in unique_counts:
                cnt -= 1
                ops += 1
            unique_counts.add(cnt)

        return ops


@pytest.mark.parametrize(
    "s,expected_output", (
        ("aab", 0),
        ("aaabbbcc", 2),
        ("ceabaacb", 2),
    )
)
def test_min_deletions(s, expected_output):
    assert Solution().minDeletions(s) == expected_output
