"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
"""
from typing import List

import pytest


class Solution:
    """
    A bit strange task. Had some difficulties removing the duplicates from
    final output.

    Time: O(n**2)
    Space: O(1)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        res = []
        i = 0

        while i < len(nums) and nums[i] <= 0:
            while 0 < i < len(nums) and nums[i] == nums[i-1]:
                i += 1

            l = i+1
            r = len(nums) - 1
            while l < r:
                sum_num = nums[i] + nums[l] + nums[r]

                if sum_num > 0:
                    r -= 1
                elif sum_num < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while 0 <= r <= len(nums) - 1 and nums[r] == nums[r + 1]:
                        r -= 1
            i += 1

        return res





@pytest.mark.parametrize(
    "nums,expected_result", (
            ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
            ([0, 0, 0], [[0, 0, 0]]),
            ([0, 0, 0, 0], [[0, 0, 0]]),
            ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
    )
)
def test_search(nums, expected_result):
    assert Solution().threeSum(nums) == expected_result
