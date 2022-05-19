"""
Given an array nums with n objects colored red, white, or blue, sort them
in-place so that objects of the same color are adjacent, with the colors in the
order red, white, and blue. We will use the integers 0, 1, and 2 to represent
the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

Follow up: Could you come up with a one-pass algorithm using only constant
extra space?
"""
from collections import Counter
from typing import List

import pytest


class Solution:
    """Count numbers and overwrite the array slots
    Time: O(n)
    Space: O(1)
    """
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = Counter(nums)
        start = 0
        i = 0

        for num in (0, 1, 2):
            count = counts[num]
            while i < count + start:
                nums[i] = num
                i += 1
            start = i


class Solution2:
    """Dutch flag algorithm, use mid pointer and decide on which direction to
    swap based on the number.
    Time: O(n)
    Space: O(1)
    """
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, mid, right = 0, 0, len(nums)-1

        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1


@pytest.mark.parametrize(
    "solution", (Solution, Solution2)
)
@pytest.mark.parametrize(
    "nums,expected_output",
    (
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
    )
)
def test_sort_colors(solution, nums, expected_output):
    solution().sortColors(nums)
    assert nums == expected_output
