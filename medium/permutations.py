"""
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
from typing import List

import pytest


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """Backtracking solution using Swap & Track method."""
        def permutate(nums: List[int], used: int) -> List[List[int]]:
            res = []
            if used == len(nums)-1:
                return [nums]

            for i in range(used, len(nums)):
                # swap num[i] to the beginning of nums to use in permutation
                nums[used], nums[i] = nums[i], nums[used]
                for sol in permutate(nums, used+1):
                    res.append(sol[:])  # use copy to avoid mutability issues

                # swap it back when permutation has been calculated
                nums[i], nums[used] = nums[used], nums[i]

            return res

        return permutate(nums, 0)


@pytest.mark.parametrize(
    "input_list,expected_list",
    (
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]),
        ([1], [[1]]),
        ([5, 6], [[5, 6], [6, 5]]),

    )
)
def test_combine(input_list, expected_list):
    assert Solution().permute(input_list) == expected_list
