"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown
pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k],
nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For
example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become
[4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1


Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""
from typing import List

import pytest


class Solution:
    """First iteration on problem.
    The idea is to find the lowest number using binary search and then apply
    search as to not-rotated array.
    Time: O:(2logn) = (logn) Using bunary search twice
    Space: O(1)  # no additional space is used
    """
    def find_lowest(self, nums: List[int]):
        l, r, = 0, len(nums) - 1
        lowest = 0

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < nums[lowest]:
                lowest = mid
                r = mid
            else:
                l = mid+1

        return lowest

    def search(self, nums: List[int], target: int) -> int:
        lowest = self.find_lowest(nums)

        if target < nums[0] or lowest == 0:
            l = lowest
            r = len(nums)-1
        else:
            l = 0
            r = lowest

        while r != l:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid

        return l if nums[l] == target else -1


@pytest.mark.parametrize(
    "nums,target,expected_result", (
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([1], 1, 0),
        ([1, 3], 3, 1),
        ([3, 1], 1, 1),
        ([0], 1, -1),
    )
)
def test_search(nums, target, expected_result):
    assert Solution().search(nums, target) == expected_result
