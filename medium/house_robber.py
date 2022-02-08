"""
https://leetcode.com/problems/house-robber/
You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed, the only constraint stopping you from
robbing each of them is that adjacent houses have security systems connected
and it will automatically contact the police if two adjacent houses were broken
into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the
police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
(money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""
from functools import cache, lru_cache
from typing import List

import pytest


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Dynamic Programming solution.
        Time: O(n)
        Space: O(1)
        """

        money_house_before = nums[0]
        money_two_houses_before = 0

        for i in range(1, len(nums)):
            money = max(nums[i] + money_two_houses_before, money_house_before)

            money_two_houses_before = money_house_before
            money_house_before = money

        return max(money_house_before, money_two_houses_before)


class Solution2:
    def rob(self, nums: List[int]) -> int:
        """
        Depth-fist search with memorization.
        Time: O(n)
        Space: O(n)
        """
        @lru_cache()
        def rob_the_house(curr: int) -> int:
            if curr == len(nums) - 1:
                return nums[curr]

            next_house = rob_the_house(curr+1)
            another_house = 0
            if curr < len(nums) - 2:
                another_house = rob_the_house(curr+2)

            return max(next_house, another_house + nums[curr])

        return rob_the_house(0)


@pytest.mark.parametrize(
    "solution", (Solution, Solution2)
)
@pytest.mark.parametrize(
    "nums,expected_output",
    (
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([2, 7, 9, 6, 1], 13),
        ([0], 0),
        ([1], 1),
    )
)
def test_rob(solution, nums, expected_output):
    assert solution().rob(nums) == expected_output
