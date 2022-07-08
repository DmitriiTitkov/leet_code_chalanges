"""
There is a row of m houses in a small city, each house must be painted with
one of the n colors (labeled from 1 to n), some houses that have been painted
last summer should not be painted again.

A neighborhood is a maximal group of continuous houses that are painted with
the same color.

For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods
[{1}, {2,2}, {3,3}, {2}, {1,1}].
Given an array houses, an m x n matrix cost and an integer target where:

houses[i]: is the color of the house i, and 0 if the house is not painted yet.
cost[i][j]: is the cost of paint the house i with the color j + 1.
Return the minimum cost of painting all the remaining houses in such a way that
there are exactly target neighborhoods. If it is not possible, return -1.



Example 1:

Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5,
n = 2, target = 3
Output: 9
Explanation: Paint houses of this way [1,2,2,1,1]
This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.
Example 2:

Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5,
n = 2, target = 3
Output: 11
Explanation: Some houses are already painted, Paint the houses of this way
[2,2,1,2,2]
This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}].
Cost of paint the first and last house (10 + 1) = 11.
Example 3:

Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4,
n = 3, target = 3
Output: -1
Explanation: Houses are already painted with a total of 4 neighborhoods
[{3},{1},{2},{3}] different of target = 3.

Constraints:
m == houses.length == cost.length
n == cost[i].length
1 <= m <= 100
1 <= n <= 20
1 <= target <= m
0 <= houses[i] <= n
1 <= cost[i][j] <= 104
"""
from typing import List

import pytest


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        def min_cost(house: int = 0, prev_color: int = 0, neiberhood_num: int = 1, memo=None) -> int:
            if memo is None:
                memo = {}

            if (house, prev_color, neiberhood_num) in memo:
                return memo[(house, prev_color, neiberhood_num)]

            if house == len(houses):
                return 0 if neiberhood_num == target else float('inf')

            if neiberhood_num > target:
                return float('inf')

            if houses[house] != 0:
                next_neiberhood_num = neiberhood_num
                if house > 0 and houses[house] != prev_color:
                    next_neiberhood_num += 1
                return min_cost(
                    house + 1,
                    houses[house],
                    next_neiberhood_num,
                    memo
                )

            minimum_cost = float('inf')
            for i in range(0, n):
                next_neiberhood_num = neiberhood_num
                if house > 0 and i + 1 != prev_color:
                    next_neiberhood_num += 1

                next_cost = min_cost(house + 1, i + 1, next_neiberhood_num, memo)
                cur_cost = cost[house][i]
                if next_cost + cur_cost <= minimum_cost:
                    minimum_cost = next_cost + cur_cost

            memo[(house, prev_color, neiberhood_num)] = minimum_cost

            return memo[(house, prev_color, neiberhood_num)]

        res = min_cost(0, houses[0])
        return res if res != float('inf') else -1


@pytest.mark.parametrize(
    "houses,cost,m,n,target,expected_result", (
        ([0, 0, 0, 0, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3, 9),
        ([0, 2, 1, 2, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3, 11),
        ([3, 1, 2, 3], [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], 4, 3, 3, -1),
    )
)
def test_min_cost(houses, cost, m, n, target, expected_result):
    assert Solution().minCost(houses, cost, m, n, target) == expected_result
