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
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0

        while nums[i] < 0:
            l = i + 1
            r = i + 2

            while l < r:
                op_num = - nums[i]
                if nums[l] + nums[r] == op_num:
                    res.append([nums[i], nums[l], nums[r]])
                    break

                elif r + 1 <= len(nums) - 1 and nums[l] + nums[r+1] <= op_num:
                    r+=1
                else:
                    l+=1

            i += 1

        return res





@pytest.mark.parametrize(
    "nums,expected_result", (
            ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    )
)
def test_search(nums, expected_result):
    assert Solution().threeSum(nums) == expected_result
