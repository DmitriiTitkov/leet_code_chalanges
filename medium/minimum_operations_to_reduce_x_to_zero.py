"""
You are given an integer array nums and an integer x. In one operation, you can
either remove the leftmost or the rightmost element from the array nums and
subtract its value from x. Note that this modifies the array for future
operations. Return the minimum number of operations to reduce x to exactly 0 if
it is possible, otherwise, return -1.

Example 1:
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce
x to zero.

Example 2:
Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example 3:
Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the
first two elements (5 operations in total) to reduce x to zero.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109
"""

from functools import cache
from typing import List
import pytest


class Solution:
    """
    DP with tabulation. Got TLE error.
    Time: O(x * n)
    Space: O(x * 3) = O(x)
    x - target num
    n - length of nums array
    """
    def minOperations(self, nums: List[int], x: int) -> int:
        length = len(nums)
        dp = [[-1, 0, length-1] for _ in range(x+1)]
        dp[0] = [0, 0, length-1]

        for i in range(x+1):
            ops_count, left, right = dp[i]
            if ops_count == -1 or left > right:
                continue

            for num, l, r in ((nums[left], left+1, right), (nums[right], left, right-1)):
                if i+num > x:
                    continue

                if dp[i+num][0] == -1 or dp[i+num][0] > ops_count+1:
                    dp[i+num] = [ops_count+1, l, r]

        return dp[x][0]


class Solution2:
    """
    DP with memoization, Got TLE.
    Time: O(min(x, n) ^ 2)
    Space: O(x * n)
    x - target num
    n - length of nums array
    """
    def minOperations(self, nums: List[int], x: int) -> int:

        @cache
        def min_ops_recursive(x, l, r) -> int:
            if x == 0:
                return 0
            if x < 0 or l > r:
                return -1

            ops_left = min_ops_recursive(x-nums[l], l+1, r)
            ops_right = min_ops_recursive(x-nums[r], l, r-1)

            if ops_left == ops_right == -1:
                ops_count = -1
            elif ops_left > -1 and ops_right > -1:
                ops_count = min(ops_left, ops_right) + 1
            else:
                ops_count = max(ops_left, ops_right) + 1
            return ops_count

        return min_ops_recursive(x, 0, len(nums)-1)



class Solution3:
    """
    As we need to find minimum amount of items at the edges of nums that sum
    to x, we can invert logic and find maximum sub array that sums to
    sum(nums) - x.
    Time: O(n)
    Space: O(1)
    """
    def minOperations(self, nums: List[int], x: int) -> int:
        required_sum = sum(nums) - x
        l = 0

        max_arr_size = 0
        cur_sum = 0
        found = False

        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum > required_sum and l <= r:
                cur_sum -= nums[l]
                l += 1

            if cur_sum == required_sum:
                found = True
                max_arr_size = max(max_arr_size, r - l + 1)

        return len(nums) - max_arr_size if found else -1


@pytest.mark.parametrize(
    "nums,x,expected_output",(
        ([1,1,4,2,3], 5, 2),
        ([5,6,7,8,9], 4, -1),
        ([3,2,20,1,1,3], 10, 5),
    )
)
def test_min_operations(nums, x, expected_output):
    assert Solution3().minOperations(nums, x) == expected_output
