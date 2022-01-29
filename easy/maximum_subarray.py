"""
Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution, try coding another
solution using the divide and conquer approach, which is more subtle.
"""
from typing import List

import pytest


class Solution:
    """
    Kadane's algorithm.
    The main idea is to iterate over array. On each iteration we find largest
    sum of subarray. As we already now the previous largest sum - 'x' we have
    only two options 'x+n' or 'n' where n is current number in the array.
    """
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_arr = nums[0]
        previous_max = float('-inf')

        for n in nums:
            previous_max = max(previous_max+n, n)
            max_sub_arr = max(previous_max, max_sub_arr)

        return max_sub_arr


@pytest.mark.parametrize(
    "nums,expected_output",
    (
            ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            ([1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4], 6),
            ([2, -3, 1, 3, -3, 2, 2, 1], 6),
            ([5, 4, -1, 7, 8], 23),
            ([-1], -1),
            ([-1, -2], -1),
            ([-2, -1, -2], -1),

    )
)
def test_combine(nums, expected_output):
    assert Solution().maxSubArray(nums) == expected_output
