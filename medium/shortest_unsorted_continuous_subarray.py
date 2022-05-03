"""
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/solution/

Given an integer array nums, you need to find one continuous subarray that if
you only sort this subarray in ascending order, then the whole array will be
sorted in ascending order.
Return the shortest such subarray and output its length.

Example 1:
Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
whole array sorted in ascending order.

Example 2:
Input: nums = [1,2,3,4]
Output: 0

Example 3:
Input: nums = [1]
Output: 0

Constraints:
1 <= nums.length <= 104
-105 <= nums[i] <= 105

Follow up: Can you solve it in O(n) time complexity?
"""
from typing import List

import pytest


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        length = len(nums)

        # find right boundary
        cur_right_edge = 0
        cur_max_num = float("-inf")

        for i in range(length):
            cur_max_num = max(cur_max_num, nums[i])

            if cur_max_num > nums[i]:
                cur_right_edge = i

        # find left boundary
        cur_left_edge = length - 1
        cur_min_num = float("inf")

        for i in range(length - 1, -1, -1):
            cur_min_num = min(cur_min_num, nums[i])

            if cur_min_num < nums[i]:
                cur_left_edge = i

        if cur_left_edge < cur_right_edge:
            return cur_right_edge - cur_left_edge + 1

        return 0


@pytest.mark.parametrize(
    "nums,expected_output",
    (
        ([1], 0),
        ([2, 6, 4, 8, 10, 9, 15], 5),
        ([1, 2, 3, 4], 0),
    )
)
def test_find_unsorted_subarray(nums, expected_output):
    assert Solution().findUnsortedSubarray(nums) == expected_output
