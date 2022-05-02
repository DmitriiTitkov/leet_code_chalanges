"""
Given an integer array nums, move all the even integers at the beginning of the
array followed by all the odd integers.
Return any array that satisfies this condition.

Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be
accepted.

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 5000
0 <= nums[i] <= 5000
"""
from typing import List

import pytest


class Solution:
    """
    Use two pointers and swap numbers if needed.
    Time: O(n)
    Space: O(1)
    """
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        while True:
            while left < len(nums) and nums[left] % 2 == 0:
                left += 1

            while right >= 0 and nums[right] % 2 != 0:
                right -= 1

            if left >= right:
                break

            nums[left], nums[right] = nums[right], nums[left]

        return nums


@pytest.mark.parametrize(
    """nums,expected_output""",
    (
        ([3, 1, 2, 4], [4, 2, 1, 3]),
    )

)
def test_sort_by_parity(nums, expected_output):
    assert Solution().sortArrayByParity(nums) == expected_output
