"""
https://leetcode.com/problems/container-with-most-water/
You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the
container contains the most water. Return the maximum amount of water a
container can store. Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array
[1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""
from typing import List

import pytest


class Solution:
    """
    Use two pointers on both ends of the array an move one that points to smaller
    value closer to center.
    Time: O(n)
    Space: O(1)
    """
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            new_area = (right - left) * min([height[left], height[right]])
            area = max([area, new_area])

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area


@pytest.mark.parametrize(
    "height,expected_output",
    (
        ([], 0),
        ([1, 1], 1),
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    )
)
def test_max_area(height, expected_output):
    assert Solution().maxArea(height) == expected_output
