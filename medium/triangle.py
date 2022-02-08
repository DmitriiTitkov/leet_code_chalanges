"""
https://leetcode.com/problems/triangle/
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. More
formally, if you are on index i on the current row, you may move to either
index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11

Example 2:
Input: triangle = [[-10]]
Output: -10


Constraints:
1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104

Follow up: Could you do this using only O(n) extra space, where n is the total
number of rows in the triangle?
"""
from typing import List

import pytest


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        DP solution.
        Time: O(n)
        Space: O(1), As mutating original data structure, however if it's
        impossible to mutate it Space Complexity is going to be O(n). Because we
        need to store all minimal paths for each position at the triangle.
        """
        for row in range(1, len(triangle)):
            for pos in range(row+1):
                prev_left = float('inf')
                prev_right = float('inf')
                if pos != 0:
                    prev_left = triangle[row-1][pos-1]

                if pos != row:
                    prev_right = triangle[row-1][pos]

                min_path = min((prev_left, prev_right)) + triangle[row][pos]
                triangle[row][pos] = min_path

        return min(triangle[-1])


@pytest.mark.parametrize(
    "triangle,expected_output",
    (
        ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11),
        ([[1]], 1),
    )
)
def test_minimum_total(triangle, expected_output):
    assert Solution().minimumTotal(triangle) == expected_output
