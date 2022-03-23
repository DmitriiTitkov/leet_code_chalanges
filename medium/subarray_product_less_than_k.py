"""
Given an array of integers nums and an integer k, return the number of
contiguous subarrays where the product of all the elements in the subarray is
strictly less than k.

Example 1:
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less
than k.

Example 2:
Input: nums = [1,2,3], k = 0
Output: 0

Constraints:
1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106
"""

from typing import List

import pytest


class Solution:
    """Use sliding window to add new product to result counter
    res += right - left + 1 - this part is a bit tricky but it will add only new
    products to result counter
    Time: O(n)
    Space: O(1)
    """
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        product = 1
        res = 0

        for right, num in enumerate(nums):
            product *= num

            if product >= k:
                product /= nums[left]
                left += 1

            res += right - left + 1

        return res


@pytest.mark.parametrize(
    "nums,k,expected_output",
    (
        ([10, 5, 2, 6], 100, 8),
        ([1, 2, 3], 0, 0),
    )
)
def test_num_subarray_product_less_than_k(nums, k, expected_output):
    assert Solution().numSubarrayProductLessThanK(nums, k) == expected_output

