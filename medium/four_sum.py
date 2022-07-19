"""
Given an array nums of n integers, return an array of all the unique quadruplets [
nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""
from typing import List

import pytest


class Solution:
    """
    Two pointers for broot force and two pointers to narrow window on a sorted
    array.
    Time: O(n^3)
    Space: O(1) if ignore the output

    """
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        res = []
        nums.sort()
        length = len(nums)

        for f in range(length - 3):
            if f > 0 and nums[f] == nums[f - 1]:
                continue
            s = f + 1
            l = f + 2
            while s < l:
                l, r = s + 1, len(nums) - 1

                while l < r:
                    cur_sum = nums[f] + nums[s] + nums[l] + nums[r]
                    if cur_sum == target:
                        res.append([nums[f], nums[s], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        while s < l and nums[s] == nums[s + 1]:
                            s += 1
                        l += 1
                        r -= 1

                    elif cur_sum < target:
                        l += 1
                    else:
                        r -= 1
                s += 1
        return res


@pytest.mark.parametrize(
    "nums,target,expected_output", (
        ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
        ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
    )
)
def test_four_sum(nums, target, expected_output):
    assert Solution().fourSum(nums, target) == expected_output
