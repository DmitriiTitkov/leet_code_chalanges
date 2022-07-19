"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above
it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:
1 <= numRows <= 30
"""
from typing import List

import pytest


class Solution:
    """
    Build triangle row by row
    Time: O(n*n)
    Space: O(n*n)

    """
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            res.append(list(0 for _ in range(i + 1)))

        res[0][0] = 1

        for i in range(numRows - 1):
            for j in range(i + 1):
                res[i + 1][j] += res[i][j]
                res[i + 1][j + 1] += res[i][j]

        return res


@pytest.mark.parametrize(
    "n,expected_output", (
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (1, [[1]]),
    )
)
def test_triangle(n, expected_output):
    assert Solution().generate(n) == expected_output
