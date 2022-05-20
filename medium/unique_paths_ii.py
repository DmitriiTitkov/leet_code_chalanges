"""
You are given an m x n integer array grid. There is a robot initially located
at the top-left corner (i.e., grid[0][0]). The robot tries to move to the
bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either
down or right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid. A path that
the robot takes cannot include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach
the bottom-right corner.
The testcases are generated so that the answer will be less than or equal to
2 * 109.

Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

Constraints:
m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
"""
from typing import List

import pytest

OBSTACLE = '#'


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[rows - 1][cols - 1] == 1:
            return 0

        for row in range(rows):
            for col in range(cols):
                if obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = OBSTACLE

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if row == rows - 1 and col == cols - 1:
                    obstacleGrid[row][col] = 1
                    continue

                if obstacleGrid[row][col] == OBSTACLE:
                    continue

                num_paths_below = 0
                num_paths_right = 0

                if row + 1 < rows and obstacleGrid[row + 1][col] != OBSTACLE:
                    num_paths_below = obstacleGrid[row + 1][col]

                if col + 1 < cols and obstacleGrid[row][col + 1] != OBSTACLE:
                    num_paths_right = obstacleGrid[row][col + 1]

                obstacleGrid[row][col] = num_paths_below + num_paths_right

        return obstacleGrid[0][0]

@pytest.mark.parametrize(
    "matrix,expected_output",
    (
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2),
        ([[0, 1], [0, 0]], 1),
        ([[0, 0], [0, 1]], 0),
        ([[1, 0], [0, 0]], 0),
    )
)
def test_unique_paths(matrix, expected_output):
    assert Solution().uniquePathsWithObstacles(matrix) == expected_output
