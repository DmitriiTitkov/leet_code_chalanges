from typing import List

import pytest


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        for _ in numbers:
            num_sum = numbers[l] + numbers[r]
            if num_sum == target:
                return [l + 1, r + 1]

            elif num_sum > target:
                r -= 1

            else:
                l += 1


@pytest.mark.parametrize(
    "input_list,target,expected_result",
    (
            ([2, 7, 11, 15], 9, [1, 2]),
            ([2, 3, 4], 6, [1, 3]),
            ([-1, 0], -1, [1, 2]),
            ([5, 25, 75], 100, [2, 3]),
            ([3, 24, 50, 79, 88, 150, 345], 200, [3, 6]),
            ([3, 24, 50, 79, 88, 150, 345], 200, [3, 6]),
    )
)
def test_search(input_list, target, expected_result):
    assert Solution().twoSum(input_list, target) == expected_result
