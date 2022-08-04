"""
There is a special square room with mirrors on each of the four walls. Except
for the southwest corner, there are receptors on each of the remaining corners,
 numbered 0, 1, and 2.
The square room has walls of length p and a laser ray from the southwest corner
first meets the east wall at a distance q from the 0th receptor.
Given the two integers p and q, return the number of the receptor that the ray
meets first.
The test cases are guaranteed so that the ray will meet a receptor eventually.

Example 1:
Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to
the left wall.

Example 2:
Input: p = 3, q = 1
Output: 1


Constraints:

1 <= q <= p <= 1000
"""
import pytest


class Solution:
    """Instead of trying calculate all possible reflection angles we can reflect
    the square and keep doing so until a corner is hit.
    Time: O(p)
    Space: O(1)
    """
    def mirrorReflection(self, p: int, q: int) -> int:
        cur = 0
        side = -1

        while True:
            if cur % p != 0 or (side < 0 and (cur / p) % 2 == 0):
                side *= -1
                cur += q
                continue

            if side < 0:
                return 2

            if (cur / p) % 2 == 0:
                return 0

            return 1


@pytest.mark.parametrize(
    "p,q,expected_output", (
        (2,1,2),
        (3,1,1),
    )
)
def test_mirror_reflections(p, q, expected_output):
    assert Solution().mirrorReflection(p, q) == expected_output
