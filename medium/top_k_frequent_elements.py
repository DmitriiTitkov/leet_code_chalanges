"""
https://leetcode.com/problems/top-k-frequent-elements/
Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n),
where n is the array's size.
"""
from collections import Counter
from typing import List

import pytest
from itertools import chain


class Solution:
    """
    Use bucket sort
    Time: O(n)
    Space: O(n)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        frequency = [[] for _ in range(length)]
        counts = Counter(nums)

        for num, count in counts.items():
            frequency[count - 1].append(num)

        flat_count = list(chain(*frequency))
        return flat_count[len(flat_count) - k:]


@pytest.mark.parametrize(
    "nums,k,expected_output",
    (
        ([1, 1, 1, 2, 2, 3], 2, [2, 1]),
        ([1], 1, [1]),
    )
)
def test_top_k_frequent(nums, k, expected_output):
    assert  Solution().topKFrequent(nums, k) == expected_output
