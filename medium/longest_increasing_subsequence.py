"""
Given an integer array nums, return the length of the longest strictly
increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some
or no elements without changing the order of the remaining elements. For
example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 104

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time
"""
from bisect import bisect, bisect_left
from functools import lru_cache
from typing import List

import pytest


class Solution:
    """
    DP Solution.
    Time: O(n*n)
    Space: O(n)
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for index in range(len(nums) - 1, -1, -1):
            for s_index in range(index, len(nums)):
                if nums[index] < nums[s_index]:
                    dp[index] = max((dp[s_index] + 1, dp[index]))

        return max(dp)


class Solution2:
    """
    DFS
    Time: O(n*n)
    Space: O()
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dfs(index):
            longest = 1
            for i in range(index+1, len(nums)):
                if nums[i] > nums[index]:
                    longest = max((dfs(i) + 1, longest))

            return longest

        longest = 1
        for i in range(len(nums)):
            longest = max((dfs(i), longest))
        return longest


class Solution3:
    """
    Greedy with binary search.
    Time: O(N * logN)
    Space: O(N)
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []

        for i in range(len(nums)):
            if not lis or lis[-1] < nums[i]:
                lis.append(nums[i])
            elif lis[-1] > nums[i]:
                new_i = bisect_left(lis, nums[i])
                lis[new_i] = nums[i]

        return len(lis)



@pytest.mark.parametrize(
    "solution", [Solution, Solution2, Solution3]
)
@pytest.mark.parametrize(
    "nums,expected_result", (
        ([2, 5, 3, 7, 101, 18], 4),
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
        ([4,10,4,3,8,9], 3),
    )
)
def test_length_of_lis(solution, nums, expected_result):
    assert solution().lengthOfLIS(nums) == expected_result
