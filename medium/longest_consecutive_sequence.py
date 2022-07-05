"""
Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence. You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List

import pytest


class Solution:
    """
    Use set to find increasing sequences. Two nested loops keep track of the
    beginning of the sequence to make sure that complexity remains linear, thus
    second loop will start only for beginning of the sequence.
    Time: O(n)
    Space: O(n)

    n - length of nums
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_seq = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                cur_seq = 1

                while num + 1 in nums_set:
                    num = num + 1
                    cur_seq += 1

                longest_seq = max(longest_seq, cur_seq)

        return longest_seq


@pytest.mark.parametrize(
    "nums,expected_output", (
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    )

)
def test_longest_consecutive(nums, expected_output):
    assert Solution().longestConsecutive(nums) == expected_output
