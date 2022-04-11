"""
https://leetcode.com/problems/combination-sum-ii/
Given a collection of candidate numbers (candidates) and a target number
(target), find all unique combinations in candidates where the candidate
numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]

Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
from collections import Counter
from typing import List, Dict

import pytest


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(choices: Dict[int, int], comb: List[int], cur_sum: int, start: int):
            if cur_sum > target:
                return
            elif cur_sum == target:
                res.append(comb[:])
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                if choices[num] == 0:
                    continue

                if i > 0 and candidates[i] == candidates[i - 1]:
                    continue

                comb.append(num)
                choices[num] -= 1

                backtrack(choices, comb, cur_sum + num, i)

                comb.pop()
                choices[num] += 1

        candidates.sort()
        backtrack(Counter(candidates), [], 0, 0)

        return res


@pytest.mark.parametrize(
    "candidates,target,expected_output",
    (
            ([10, 1, 2, 7, 6, 1, 5], 8,
             [
                 [1, 1, 6],
                 [1, 2, 5],
                 [1, 7],
                 [2, 6]
             ]
             ),
            ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),
    ),
)
def test_combination_sum(candidates, target, expected_output):
    assert Solution().combinationSum2(candidates, target) == expected_output
