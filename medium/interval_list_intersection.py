"""
https://leetcode.com/problems/interval-list-intersections/
You are given two lists of closed intervals, firstList and secondList, where
firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of
intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with
a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are
either empty or represented as a closed interval. For example, the intersection
of [1, 3] and [2, 4] is [2, 3].



Example 1:
Input: firstList = [[0,2],[5,10],[13,23],[24,25]],
       secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Example 2:
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []

Constraints:
0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= starti < endi <= 109
endi < starti+1
0 <= startj < endj <= 109
endj < startj+1
"""
from typing import List

import pytest


class Solution:
    """
    Find all intersecting intervals by checking pairs and incrementing cursor of
    lower interval.
    Time: O(mn)
    Space: O(mn)  # max answer size
    """
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        left_curr = right_curr = 0
        res = []

        while left_curr < len(firstList) and right_curr < len(secondList):
            left_interval = firstList[left_curr]
            right_interval = secondList[right_curr]

            if left_interval[0] > right_interval[1]:
                right_curr += 1
                continue

            if left_interval[1] < right_interval[0]:
                left_curr += 1
                continue

            interval_start = max([left_interval[0], right_interval[0]])
            interval_end = min([left_interval[1], right_interval[1]])
            res.append([interval_start, interval_end])

            if left_interval[1] > right_interval[1]:
                right_curr += 1
            else:
                left_curr += 1

        return res


@pytest.mark.parametrize(
    "first,second,expected_result",
    (
        ([], [], []),
        ([[2, 10]], [], []),
        (
            [[0, 2], [5, 10], [13, 23], [24, 25]],
            [[1, 5], [8, 12], [15, 24], [25, 26]],
            [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]],
        )
    )
)
def test_interval_intersection(first, second, expected_result):
    assert Solution().intervalIntersection(first, second) == expected_result
