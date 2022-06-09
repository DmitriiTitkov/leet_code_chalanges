"""
partition-equal-subset-sum
Given a non-empty array nums containing only positive integers, find if the
array can be partitioned into two subsets such that the sum of elements in both
subsets is equal.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100
"""
from functools import cache
from typing import List

import pytest


class Solution:
    """
    Memoization
    Time: O(n*k)
    Space: O(k)

    n - length of nums
    k - partition size
    """
    def canPartition(self, nums: List[int]) -> bool:
        full_size = sum(nums)
        if full_size % 2 != 0:
            return False

        part_size = full_size / 2

        @cache
        def sum_partition(start, size: int) -> bool:
            if size < 0:
                return False
            if size == 0:
                return True

            for i in range(start, len(nums)):
                res = sum_partition(i + 1, size - nums[i])
                if res:
                    return True

            return False

        return sum_partition(0, part_size)


@pytest.mark.parametrize(
    "nums,expected_output", (
        ([1, 5, 11, 5], True),
        ([1, 2, 3, 5], False),
    )
)
def test_can_partition(nums, expected_output):
    assert Solution().canPartition(nums) == expected_output
