"""
You are given an integer array nums. You are initially positioned at the
array's first index, and each element in the array represents your maximum jump
length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump
length is 0, which makes it impossible to reach the last index.

Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 105
"""
from typing import List

import pytest


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur = 0
        right_boundry = 0

        while cur <= right_boundry:
            if cur == len(nums) - 1:
                return True
            right_boundry = max((
                right_boundry,
                cur + nums[cur]
            ))
            cur += 1

        return False


@pytest.mark.parametrize(
    "nums,expected_output",
    (
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
    )
)
def test_jump_game(nums, expected_output):
    assert Solution().canJump(nums) == expected_output
