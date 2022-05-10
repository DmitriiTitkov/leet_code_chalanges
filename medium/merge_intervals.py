"""
Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
from typing import List

import pytest


class Solution:
    """
    Use sorting and then merge adjustent intervals.
    Time: O(n log n)
    Space: O(n) - store final result
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        non_overlaping = [intervals[0]]
        prev_start, prev_end = intervals[0][0], intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]

            if prev_start <= start <= prev_end:
                non_overlaping.pop()
                start = min(prev_start, start)
                end = max(prev_end, end)

            non_overlaping.append([start, end])
            prev_start, prev_end = start, end

        return non_overlaping


@pytest.mark.parametrize(
    "intervals,expected_output",
    (
        (
            [[1, 3], [2, 6], [8, 10], [15, 18]],
            [[1, 6], [8, 10], [15, 18]],
        ),
        (
            [[1, 4], [4, 5]],
            [[1, 5]],
        ),
    )
)
def test_combination_sum(intervals, expected_output):
    assert Solution().merge(intervals) == expected_output
