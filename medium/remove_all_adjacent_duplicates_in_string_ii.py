"""
You are given a string s and an integer k, a k duplicate removal consists of c
hoosing k adjacent and equal letters from s and removing them, causing the left
and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is
guaranteed that the answer is unique.

Example 1:
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Example 2:
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation:
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Example 3:
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"

Constraints:
1 <= s.length <= 105
2 <= k <= 104
s only contains lower case English letters.
"""
import pytest


class Solution:
    """
    Use stack to store letter counts.
    Time: O(n)
    Space: O(n)
    """
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for letter in s:
            if not stack:
                stack.append((letter, 1))
                continue

            prev_letter = stack[-1][0]
            prev_count = stack[-1][1]

            if letter == prev_letter:
                count = prev_count + 1
            else:
                count = 1

            if count == k:
                for _ in range(k - 1):
                    stack.pop()
                continue

            stack.append((letter, count))

        return "".join(x[0] for x in stack)


class Solution2:
    """
    Use stack to store letter counts. Space is optimised to store letter count
    in a single frame.
    Time: O(n)
    Space: O(n) - Optimised
    """
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for letter in s:
            if not stack:
                stack.append([letter, 1])
                continue

            prev_letter = stack[-1][0]

            if letter == prev_letter:
                stack[-1][1] += 1
            else:
                stack.append([letter, 1])

            prev_count = stack[-1][1]
            if prev_count == k:
                stack.pop()

        return "".join(letter * count for letter, count in stack)


@pytest.mark.parametrize(
    "solution", [Solution, Solution2]
)
@pytest.mark.parametrize(
    "s,k,expected_output",
    (
        ("abcd", 2, "abcd"),
        ("deeedbbcccbdaa", 3, "aa"),
        ("pbbcggttciiippooaais", 2, "ps"),
    )
)
def test_remove_duplicates(solution, s, k, expected_output):
    assert solution().removeDuplicates(s, k) == expected_output
