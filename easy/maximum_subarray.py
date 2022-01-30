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
    Time: O(n)
    Space: O(1)
    """
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_arr = nums[0]
        previous_max = float('-inf')

        for n in nums:
            previous_max = max(previous_max+n, n)
            max_sub_arr = max(previous_max, max_sub_arr)

        return max_sub_arr


class Solution2:
    """
    Naive approach.
    In naive approach we bruteforce all possible sub-arrays and find larges sum.

    Time: O(n^2)
    Space: O(1)
    """
    def maxSubArray(self, nums: List[int]) -> int:
        max_cont_sub = float('-inf')
        for i, n in enumerate(nums):
            max_sub_arr = n
            las_sub_arr_sum = n
            for sub_i in range(i+1, len(nums)):
                # instead of using max we can iterate and combine numbers which
                # results in O(n^3)
                max_sub_arr = max(max_sub_arr, las_sub_arr_sum+nums[sub_i])
                las_sub_arr_sum = las_sub_arr_sum+nums[sub_i]

            max_cont_sub = max(max_cont_sub, max_sub_arr)
        return max_cont_sub


class Solution3:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Divide and Conquer. split array in halfs and calculate each half
        recursively. For each execution choose max of lms, rms, cms where:
        lms: Maximum sum in left subarray
        rms: Maximum sum in right subarray
        cms: Maximum sum of cross-section array(Array that starts in left half
        and ends in right half).

        """

        def max_sub(nums: List[int]) -> int:
            if len(nums) == 1:
                return nums[0]

            mid = len(nums) // 2

            lms = max_sub(nums[0:mid])
            rms = max_sub(nums[mid:])

            max_l = nums[mid-1]
            cur_sum = nums[mid-1]
            for i in range(mid-2, -1, -1):
                cur_sum += nums[i]
                max_l = max(cur_sum, max_l)

            max_r = nums[mid]
            cur_sum = nums[mid]
            for i in range(mid+1, len(nums)):
                cur_sum += nums[i]
                max_r = max(cur_sum, max_r)

            cms = max_l + max_r
            return max(lms, rms, cms)

        return max_sub(nums)



@pytest.mark.parametrize(
    'solution', (Solution, Solution2)
)
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
def test_combine(solution, nums, expected_output):
    assert solution().maxSubArray(nums) == expected_output
