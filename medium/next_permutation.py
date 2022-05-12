"""
A permutation of an array of integers is an arrangement of its members into a
sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of
arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically
greater permutation of its integer. More formally, if all the permutations of
the array are sorted in one container according to their lexicographical order,
then the next permutation of that array is the permutation that follows it in
the sorted container. If such arrangement is not possible, the array must be
rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not
have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""
from typing import List

import pytest


class Solution:
    """
    The idea is to iterate from right to left in permutation until we find first
    number that is less than any number on the right. Then starting from the
    number iterate left to right and find minimal possible number that can is
    greater than found number(pivot variable). Swap two found numbers and then
    revert right part of the list as it must be in decreasing order.

    Time: O(n)
    Space: O(1)
    """
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        max_num = nums[length - 1]
        pivot_index = None

        for i in range(length - 2, -1, -1):
            if nums[i] < max_num:
                pivot_index = i
                break
            max_num = max(max_num, nums[i])

        if pivot_index is None:
            nums.reverse()
            return

        pivot = nums[pivot_index]
        min_gt_pivot = float("inf")
        min_gt_pivot_index = pivot

        for i in range(pivot_index + 1, length):
            if nums[i] > pivot:
                new_min_gt_pivot = min(min_gt_pivot, nums[i])
                if new_min_gt_pivot <= min_gt_pivot:
                    min_gt_pivot = new_min_gt_pivot
                    min_gt_pivot_index = i

        nums[pivot_index], nums[min_gt_pivot_index] = nums[min_gt_pivot_index], nums[pivot_index]

        self.reverse_sublist(nums, pivot_index + 1, length - 1)

    def reverse_sublist(self, nums, start, finish):
        while start < finish:
            nums[start], nums[finish] = nums[finish], nums[start]
            start += 1
            finish -= 1


@pytest.mark.parametrize(
    "nums,expected_output",(
        (
            [1, 2, 3],
            [1, 3, 2],
        ),
        (
            [3, 2, 1],
            [1, 2, 3],
        ),
        (
            [1, 1, 5],
            [1, 5, 1],
        ),
    )
)
def test_next_permutation(nums, expected_output):
    Solution().nextPermutation(nums)
    assert nums == expected_output
