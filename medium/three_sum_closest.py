"""
Given an integer array nums of length n and an integer target, find three
integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0

Constraints
3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""
from typing import List

import pytest


class Solution:
    """
    Consider every num in sorted nums and use two pointers to narrow the window
    Time: O(n**2)
    Space: O(1)
    """
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        closest = float("inf")
        distance = float("inf")
        nums.sort()

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                cur = nums[i] + nums[l] + nums[r]
                cur_distance = abs(target - cur)
                if cur_distance < distance:
                    closest = cur
                    distance = cur_distance

                if cur <= target:
                    l += 1
                else:
                    r -= 1

        return closest


@pytest.mark.parametrize(
    "nums,target,expected_output",
    (
        ([-1, 2, 1, -4], 1, 2),
        ([0, 0, 0], 1, 0),
    )
)
def test_three_sum_closest(nums, target, expected_output):
    assert Solution().threeSumClosest(nums, target) == expected_output
