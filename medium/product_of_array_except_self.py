"""
Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i]. The product of any
prefix or suffix of nums is guaranteed to fit in a 32-bit integer. You must
write an algorithm that runs in O(n) time and without using the division
operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The
output array does not count as extra space for space complexity analysis.)
"""
from typing import List

import pytest


class Solution:
    """
    Use two arrays to calculate prefix products and suffix products.
    Time: O(n)
    Space: O(n)
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        pref = [0] * length
        suff = [0] * length
        res = [0] * length

        # populate prefix
        for i in range(length):
            prev = pref[i - 1] if i > 0 else 1
            pref[i] = prev * nums[i]

        # populate suffix
        for i in range(length - 1, -1, -1):
            prev = suff[i + 1] if i < length - 1 else 1
            suff[i] = prev * nums[i]

        # create answer
        for i in range(length):
            prev_product = pref[i - 1] if i > 0 else 1
            next_product = suff[i + 1] if i < length - 1 else 1
            res[i] = prev_product * next_product

        return res


class Solution2:
    """
    Use single output array and calculated products in place.
    Time: O(n)
    Space: O(n) / O(1) if output is not considered as extra space
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length

        # populate prefix
        for i in range(length - 1):
            res[i + 1] = res[i] * nums[i]

        # populate suffix
        prod = nums[-1]
        for i in range(length - 2, -1, -1):
            res[i] = prod * res[i]
            prod = prod * nums[i]

        return res


@pytest.mark.parametrize(
    "solution", (Solution, Solution2)
)
@pytest.mark.parametrize(
    "nums,expected_output", (
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    )
)
def test_product_except_self(solution, nums, expected_output):
    assert solution().productExceptSelf(nums) == expected_output
