"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Given an array of integers nums sorted in non-decreasing order, find the
starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
from typing import List

import pytest


class Solution:
    """
    Binary search to find leftmost index for target and leftmost index for
    target+1.
    Time: O(logn)
    Space: O(1)

    n - length of nums
    """
    def bin_search(self, nums, target) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        left = self.bin_search(nums, target)
        if nums[left] != target:
            return [-1, -1]
        right = self.bin_search(nums, target + 1)
        if nums[right] != target:
            right -= 1

        return [left, right]


@pytest.mark.parametrize(
    "nums,target,expected_output",
    (
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 10, 10], 10, [4, 5]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 8, 10, 10], 4, [10, 13]),

    )
)
def test_is_search_range(nums, target, expected_output):
    assert Solution().searchRange(nums, target) == expected_output
