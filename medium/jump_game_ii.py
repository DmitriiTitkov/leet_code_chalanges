"""
Given an array of non-negative integers nums, you are initially positioned at
the first index of the array. Each element in the array represents your maximum
jump length at that position. Your goal is to reach the last index in the
minimum number of jumps. You can assume that you can always reach the last
index.

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1
step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 1000
"""
from typing import List

import pytest


class Solution:
    """Iterate over array and remember the max jum you can make. Decrease jump
    and max jump with each step and increment total jumps when switching them.
    Time: O(n)
    Space: O(1)
    """
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        total_jumps = 1

        next_max_jump = 0
        cur_jump = nums[0]
        i = 0

        while i < len(nums) - 2:
            i += 1
            next_max_jump -= 1
            cur_jump -= 1

            next_max_jump = max((
                next_max_jump,
                nums[i]
            ))

            if cur_jump == 0:
                total_jumps += 1
                cur_jump = next_max_jump

        return total_jumps


@pytest.mark.parametrize(
    "nums,expected_output",
    (
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),

    )
)
def test_jump_game(nums, expected_output):
    assert Solution().jump(nums) == expected_output
