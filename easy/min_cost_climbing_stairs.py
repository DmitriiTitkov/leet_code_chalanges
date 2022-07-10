"""
You are given an integer array cost where cost[i] is the cost of ith step on a
staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

Constraints:
2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""
from typing import List

import pytest


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one_step_prev = 0
        two_step_prev = 0

        for step_cost in cost:
            cur_cost = min(
                one_step_prev,
                two_step_prev,

            ) + step_cost

            two_step_prev = one_step_prev
            one_step_prev = cur_cost

        return min(one_step_prev, two_step_prev)


@pytest.mark.parametrize(
    "cost,expected_result", (
        ([10, 15, 20], 15),
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
    )
)
def test_min_cost(cost, expected_result):
    assert Solution().minCostClimbingStairs(cost) == expected_result
