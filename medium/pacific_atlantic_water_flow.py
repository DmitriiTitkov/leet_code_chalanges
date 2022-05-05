"""
https://leetcode.com/problems/pacific-atlantic-water-flow/
There is an m x n rectangular island that borders both the Pacific Ocean and
Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and
the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n
integer matrix heights where heights[r][c] represents the height above sea level
of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring
cells directly north, south, east, and west if the neighboring cell's height is
less than or equal to the current cell's height. Water can flow from any cell
adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes
that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic
oceans.

Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Example 2:
Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]

Constraints:
m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
"""
from collections import deque
from typing import List


class Solution:
    """
    Time: O(mn) due to memorization
    Space: O(mn)
    """
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        num_rows = len(heights)
        num_cols = len(heights[0])

        land_from_p = set()
        land_from_a = set()

        def bfs(row, col, visited: set) -> None:
            queue = deque()
            queue.appendleft((row, col))

            while queue:
                row, col = queue.pop()
                visited.add((row, col))

                for r, c in (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1):
                    if ((r, c) not in visited and
                            0 <= r < num_rows and
                            0 <= c < num_cols and
                            heights[r][c] >= heights[row][col]
                    ):
                        queue.appendleft((r, c))
                        visited.add((r, c))

        for row in range(num_rows):
            bfs(row, 0, land_from_p)
            bfs(row, num_cols - 1, land_from_a)

        for col in range(num_cols):
            bfs(0, col, land_from_p)
            bfs(num_rows - 1, col, land_from_a)

        return land_from_p & land_from_a



