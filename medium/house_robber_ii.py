"""
You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed. All houses at this place are arranged in
a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected, and it will
automatically contact the police if two adjacent houses were broken into on the
same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the
police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3
(money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""
from typing import List

import pytest


class Solution:
    """
    DP solution
    Time: O(n) iterate twice over nums and find max
    Space: O(1)
    """
    def find_max_money(self, nums: List[int], start: int, end: int) -> int:
        two_houses_before = 0
        one_house_before = 0

        for i in range(start, end):
            money = max((
                one_house_before,
                two_houses_before + nums[i],
            ))
            two_houses_before = one_house_before
            one_house_before = money

        return max(one_house_before, two_houses_before)

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_from_first = self.find_max_money(nums, 0, len(nums) - 1)
        max_from_second = self.find_max_money(nums, 1, len(nums))

        return max(max_from_first, max_from_second)


@pytest.mark.parametrize(
    "nums,expected_output",
    (
        ([2, 3, 2], 3),
        ([1, 2, 3, 1], 4),
        ([1, 2, 3], 3),

    )
)
def test_rob(nums, expected_output):
    assert Solution().rob(nums) == expected_output
