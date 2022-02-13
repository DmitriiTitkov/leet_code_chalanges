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
    """First iteration:
    Time: O(log n)
    Space: O(log n) - for stack
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left = self.find_starting(nums, target, 0, len(nums) - 1)
        right = self.find_ending(nums, target, 0, len(nums) - 1)
        return [left, right]

    def find_starting(self, nums: List[int], target, l: int, r: int) -> int:
        if l == r:
            if nums[l] == target:
                return l
            else:
                return -1

        mid = (l+r) // 2
        if target <= nums[mid]:
            return self.find_starting(nums, target, l, mid)
        else:
            return self.find_starting(nums, target, mid+1, r)

    def find_ending(self, nums: List[int], target: int, l: int, r: int) -> int:
        if l == r:
            if nums[l] == target:
                return l
            else:
                return -1

        mid = (l + r) // 2
        if mid < 0:
            return -1
        if target >= nums[mid]:
            right = self.find_ending(nums, target, mid+1, r)
            if right == -1 and nums[mid] == target:
                return mid
            return right
        else:
            if l == mid:
                return -1
            return self.find_ending(nums, target, l, mid-1)


@pytest.mark.parametrize(
    "nums,target,expected_output",
    (
        ([5,7,7,8,8,10], 8, [3,4]),
        ([0,0,1,1,1,2,2,3,3,3,4,4,4,4,5,5,6,6,6,8,10,10], 4, [10, 13]),

    )
)
def test_is_search_range(nums, target, expected_output):
    assert Solution().searchRange(nums, target) == expected_output