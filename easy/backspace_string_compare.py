"""
Given two strings s and t, return true if they are equal when both are typed
into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

Constraints:
1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.

Follow up: Can you solve it in O(n) time and O(1) space?
"""
import pytest


def remove_backspace(string: str, cur: int) -> int:
    """Function will count all backspaced characters and return index of
    rightmost not-backspaced character"""
    backspace_count = 0
    while cur >= 0 and (string[cur] == "#" or backspace_count > 0):
        if string[cur] == "#":
            backspace_count += 1
        else:
            backspace_count -= 1
        cur -= 1
    return cur


class Solution:
    """
    Iterative solution, iterate from end to start and count backspaces
    Time: O(n)
    Space: O(1)
    """
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_curr = len(s) - 1
        t_curr = len(t) - 1

        while s_curr >= 0 or t_curr >= 0:
            s_curr = remove_backspace(s, s_curr)
            t_curr = remove_backspace(t, t_curr)

            if s[s_curr] != t[t_curr] or (s_curr >= 0) ^ (t_curr >= 0):
                return False

            s_curr -= 1
            t_curr -= 1

        return True


@pytest.mark.parametrize(
    "s,t,expected_result",
    (
        ("ab#c", "ad#c", True),
        ("ab##", "c#d#", True),
        ("a#c", "b", False),
        ("xywrrmp", "xywrrmu#p", True),
    )
)
def test_backspace_compare(s, t, expected_result):
    assert Solution().backspaceCompare(s, t) is expected_result