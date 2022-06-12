"""
You are given an array of positive integers nums and want to erase a subarray
containing unique elements. The score you get by erasing the subarray is equal
to the sum of its elements. Return the maximum score you can get by erasing
exactly one subarray. An array b is called to be a subarray of a if it forms a
contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r]
for some (l,r).

Example 1:
Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].

Example 2:
Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 104
"""
from typing import List

import pytest


class Solution:
    """
    Use sliding window to find max subarray
    Time: O(n)
    Space: O(n)
    n - number of elements in nums
    """
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        subarray = set()
        l = 0
        cur_score = 0
        max_score = 0

        for r in range(len(nums)):
            while nums[r] in subarray:
                subarray.remove(nums[l])
                cur_score -= nums[l]
                l += 1

            subarray.add(nums[r])
            cur_score += nums[r]
            max_score = max(max_score, cur_score)

        return max_score


@pytest.mark.parametrize(
    "nums,expected_output", (
        ([4, 2, 4, 5, 6], 17),
        ([5, 2, 1, 2, 5, 2, 1, 2, 5], 8),
    )
)
def test_max_unique_subarr(nums, expected_output):
    assert Solution().maximumUniqueSubarray(nums) == expected_output
