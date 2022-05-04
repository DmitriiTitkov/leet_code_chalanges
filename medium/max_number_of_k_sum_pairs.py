"""
You are given an integer array nums and an integer k. In one operation, you can
pick two numbers from the array whose sum equals k and remove them from the
array. Return the maximum number of operations you can perform on the array.

Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
"""
from collections import Counter
from typing import List

import pytest


class Solution:
    """Store counts of nums and decrease the count when a pair os found.
    Time: O(n)
    Space: O(n)
    """
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations = 0

        # create hash map to store num occurrences
        counts = Counter(nums)

        for i in range(len(nums)):
            first_num = nums[i]
            second_num = k - first_num

            if first_num == second_num and counts[first_num] >= 2:
                counts[first_num] -= 2
                operations += 1
                continue

            if first_num != second_num and counts[first_num] >= 1 and counts[second_num] >= 1:
                counts[first_num] -= 1
                counts[second_num] -= 1
                operations += 1

        return operations


@pytest.mark.parametrize(
    "nums,k,expected_output",
    (
        ([1, 2, 3, 4], 5, 2),
        ([3, 1, 3, 4, 3], 6, 1),
        ([1, 1, 1, 1, 1], 2, 2),
        ([1], 2, 0),
    )
)
def test_max_operations(nums, k, expected_output):
    assert Solution().maxOperations(nums, k) == expected_output
