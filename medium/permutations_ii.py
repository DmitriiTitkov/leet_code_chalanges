"""Given a collection of numbers, nums, that might contain duplicates, return
all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""
from collections import Counter
from typing import List, Dict

import pytest


class Solution:
    """
    Backtracking algorithm. To avoid duplicated use counter an iterate over the
    keys.
    Time: O(n * n!)
    """
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def permute(choices: Dict[int, int], per: List[int]) -> None:
            if len(per) == len(nums):
                res.append(per[:])
                return

            for num in choices:
                if choices[num] == 0:
                    continue
                choices[num] -= 1
                per.append(num)

                permute(choices, per)

                per.pop()
                choices[num] += 1

        permute(Counter(nums), [])
        return res


@pytest.mark.parametrize(
    "solution,input_list,expected_list",
    (
        (Solution, [1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        (Solution, [1], [[1]]),
        (Solution, [5, 6], [[5, 6], [6, 5]]),
        (Solution, [1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),

    )
)
def test_combine(solution, input_list, expected_list):
    assert solution().permuteUnique(input_list) == expected_list
