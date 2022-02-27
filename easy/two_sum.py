"""
https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target. You may assume that each input
would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time
complexity?
"""
from typing import List

import pytest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rev_map = {}

        for index, num in enumerate(nums):
            add_num = target - num

            if rev_map.get(add_num) is not None:
                return [index, rev_map[add_num]]

            rev_map[num] = index


@pytest.mark.parametrize(
    "nums,target,expected_result", (
            ([2, 7, 11, 15], 9, [1, 0]),
            ([3, 2, 4], 6, [2, 1]),
            ([3, 3], 6, [1, 0])
    )
)
def test_search(nums, target, expected_result):
    assert Solution().twoSum(nums, target) == expected_result