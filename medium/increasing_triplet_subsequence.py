"""
Given an integer array nums, return true if there exists a triple of indices
(i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such
indices exists, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because
nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:
1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1


Follow up: Could you implement a solution that runs in O(n) time complexity and
O(1) space complexity?
"""
from typing import List

import pytest


class Solution:
    """Use additional arrays to keep record of max on the right and min on the
    left.
    Time: O(n)
    Space: O(n)
    """
    def increasingTriplet(self, nums: List[int]) -> bool:
        length = len(nums)
        has_smaller_num = [False] * length
        has_greater_num = [False] * length

        min_num = float("inf")
        for i in range(length):
            min_num = min(min_num, nums[i])
            if nums[i] > min_num:
                has_smaller_num[i] = True

        max_num = float("-inf")
        for i in range(length - 1, -1, -1):
            max_num = max(max_num, nums[i])
            if nums[i] < max_num:
                has_greater_num[i] = True

        for i in range(length):
            if has_smaller_num[i] and has_greater_num[i]:
                return True

        return False


class Solution2:
    """
    We iterate over array and use left and mid pointers. As we have a number
    that is greater than mid we know that sequence exist. We can safely update
    left pointer as mid remains the same until more appropriate mid is found.
    Time: O(n)
    Space: O(1)
    """
    def increasingTriplet(self, nums: List[int]) -> bool:
        left = nums[0]
        mid = float("inf")

        for n in nums:
            if n < mid and n > left:
                mid = n
            elif n > mid:
                return True
            elif n < mid and n < left:
                left = n

        return False


@pytest.mark.parametrize(
    "solution", (Solution, Solution2),
)
@pytest.mark.parametrize(
    "nums,expected_output", (
        ([1, 2, 3, 4, 5], True),
        ([5, 4, 3, 2, 1], False),
        ([2, 1, 5, 0, 4, 6], True),

    )
)
def test_increasing_triplet(solution, nums, expected_output):
    assert solution().increasingTriplet(nums) == expected_output
