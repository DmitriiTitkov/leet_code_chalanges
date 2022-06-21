"""
1642. Furthest Building You Can Reach
You are given an integer array heights representing the heights of buildings,
some bricks, and some ladders. You start your journey from building 0 and move
to the next building by possibly using bricks or ladders.
While moving from building i to building i+1 (0-indexed), If the current
building's height is greater than or equal to the next building's height, you
do not need a ladder or bricks.
If the current building's height is less than the next building's height, you
can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the
given ladders and bricks optimally.

Example 1:
Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders
because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or
ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more
bricks or ladders.

Example 2:
Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7

Example 3:
Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3

Constraints:
1 <= heights.length <= 105
1 <= heights[i] <= 106
0 <= bricks <= 109
0 <= ladders <= heights.length
"""
import heapq
from functools import cache
from typing import List

import pytest


class Solution:
    """
    DP with memoization - TLE.
    Time: O(n * k * l)
    Space: O(n * k * l)
    n - length of heights array
    k - amount of bricks
    l - amount of ladders
    """
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        @cache
        def furthest_building_rec(i: int, bricks: int, ladders: int) -> int:
            if i == len(heights) - 1:
                return i

            height_diff = heights[i + 1] - heights[i]
            if height_diff > bricks and ladders == 0:
                return i

            if height_diff <= 0:
                return furthest_building_rec(i + 1, bricks, ladders)

            move_with_bricks = move_with_ladder = i
            if height_diff < bricks:
                move_with_bricks = furthest_building_rec(
                    i + 1,
                    bricks - height_diff,
                    ladders,
                )

            if ladders > 0:
                move_with_ladder = furthest_building_rec(
                    i + 1,
                    bricks,
                    ladders - 1,
                )

            return max(move_with_ladder, move_with_bricks)

        return furthest_building_rec(0, bricks, ladders)


class Solution2:
    """
    Use heap to remember largest height differences.
    Time: O(n * log l)
    Space: O(n)
    """
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = [0] * ladders

        prev_height = heights[0]

        for i, height in enumerate(heights):
            height_diff = height - prev_height
            prev_height = height

            if height_diff <= 0:
                continue

            if heap and heap[0] < height_diff:
                bricks -= heapq.heappushpop(heap, height_diff)
                if bricks < 0:
                    return i - 1
            else:
                if bricks >= height_diff:
                    bricks -= height_diff
                else:
                    return i - 1

        return i


@pytest.mark.parametrize(
    "heights,bricks,ladders,expected_output", (
        ([4, 2, 7, 6, 9, 14, 12], 5, 1, 4),
        ([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2, 7),
        ([14, 3, 19, 3], 17, 0, 3),
    )
)
def test_furthest_building(heights, bricks, ladders, expected_output):
    assert Solution2().furthestBuilding(heights, bricks, ladders) == expected_output
