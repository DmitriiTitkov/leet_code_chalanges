"""
Given an array of positive integers nums and a positive integer target, return
the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr]
of which the sum is greater than or equal to target. If there is no such
subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105

Follow up: If you have figured out the O(n) solution, try coding another
solution of which the time complexity is O(n log(n)).
"""
from typing import List

import pytest


"""
Given an array of positive integers nums and a positive integer target, return
the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr]
of which the sum is greater than or equal to target. If there is no such
subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105

Follow up: If you have figured out the O(n) solution, try coding another
solution of which the time complexity is O(n log(n)).
"""
from typing import List


class Solution:
    """Use two pointers to iterate over array and keep the window as small as
    possible by using inner loop.
    Time: O(n)
    Space: O(1)
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        subarr_sum = nums[0]
        res = float('inf')

        for right in range(len(nums)):
            subarr_sum += nums[right]

            while subarr_sum >= target:
                res = min([(right - left + 1), res])
                subarr_sum -= nums[left]
                left += 1

        return res if res != float('inf') else 0


@pytest.mark.parametrize(
    "target,nums,expected_output",
    (
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 4, 4], 1),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
    )

)
def test_min_subarr_len(target,nums,expected_output):
    assert Solution().minSubArrayLen(target, nums) == expected_output
