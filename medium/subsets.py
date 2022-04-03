"""
https://leetcode.com/problems/subsets/
Given an integer array nums of unique elements, return all possible subsets
(the power set). The solution set must not contain duplicate subsets.
Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
from typing import List

import pytest


class Solution:
    """Backtracking approach
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur_index: int, subset: List[int]) -> List[int]:
            res.append(subset[:])

            for index in range(cur_index, len(nums)):
                subset.append(nums[index])
                dfs(index + 1, subset)
                subset.pop()

        dfs(0, [])

        return res


@pytest.mark.parametrize(
    "nums, expected_result",
    (
        ([1,2,3], [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]),
        ([0], [[], [0]]),
    )
)
def test_subsets(nums, expected_result):
    assert Solution().subsets(nums) == expected_result
