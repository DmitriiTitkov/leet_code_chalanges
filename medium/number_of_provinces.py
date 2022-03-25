"""
https://leetcode.com/problems/number-of-provinces/
There are n cities. Some of them are connected, while some are not. If city a
is connected directly with city b, and city b is connected directly with city
c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other
cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the
ith city and the jth city are directly connected, and isConnected[i][j] = 0
otherwise.
Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Constraints:
1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""
from typing import List

import pytest


class Solution:
    """
    DFS with mutation of input data. Replace data in all visited cells with 0
    to avoid visiting one cell twice.
    Time: O(n * m) all cells will be visited no more than once. Where n number
          of rows and m number of columns.

    Space: O(n) Where n number of rows. Space is used by recursion stack and
           function recurse only for new rows.

    """
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0

        def find_province(row, col) -> int:
            if isConnected[row][col] == 0:
                return 0

            isConnected[row][col] = 0

            for c in range(0, len(isConnected[row])):
                if isConnected[row][c] == 1:
                    find_province(c, c)

            return 1

        for row in range(len(isConnected)):
            res += find_province(row, row)

        return res


@pytest.mark.parametrize(
    "grid,expected_result",
    (
        (
            [[1, 1, 0], [1, 1, 0], [0, 0, 1]],
            2
        ),
        (
            [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            3
        ),

    )

)
def test_find_circle_num(grid, expected_result):
    assert Solution().findCircleNum(grid) == expected_result
