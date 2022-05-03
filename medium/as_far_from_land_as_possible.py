"""
https://leetcode.com/problems/as-far-from-land-as-possible/

Given an n x n grid containing only values 0 and 1, where 0 represents water
and 1 represents land, find a water cell such that its distance to the nearest
land cell is maximized, and return the distance. If no land or water exists in
the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance
between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

Example 1:
Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.

Example 2:
Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.


Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""
from typing import List


class Solution:
    """
    DP Solution
    Time: O(n) - traverse three times
    Space: O(n) - store distance in the grid
    """
    def maxDistance(self, grid: List[List[int]]) -> int:
        length = len(grid)

        distance_grid = [[float("inf")] * length for n in range(length)]

        for row in range(length):
            for col in range(length):
                if grid[row][col] == 1:
                    distance_grid[row][col] = 0
                    continue

                if row > 0:
                    distance_grid[row][col] = distance_grid[row - 1][col] + 1

                if col > 0:
                    distance_grid[row][col] = min(distance_grid[row][col - 1] + 1, distance_grid[row][col])

        for row in range(length - 1, -1, -1):
            for col in range(length - 1, -1, -1):
                if grid[row][col] == 1:
                    distance_grid[row][col] = 0
                    continue

                if row < length - 1:
                    distance_grid[row][col] = min(distance_grid[row + 1][col] + 1, distance_grid[row][col])

                if col < length - 1:
                    distance_grid[row][col] = min(distance_grid[row][col + 1] + 1, distance_grid[row][col])

        max_distance_from_land = -1
        has_land = False
        has_water = False

        for row in range(length):
            for col in range(length):
                if grid[row][col] == 1:
                    has_land = True
                if grid[row][col] == 0:
                    has_water = True
                max_distance_from_land = max(max_distance_from_land, distance_grid[row][col])

        return max_distance_from_land if has_land and has_water else -1
