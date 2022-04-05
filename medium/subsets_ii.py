from typing import List

import pytest


class Solution:
    """
    Space complexity somewhere near exponential, should be little less as
    the paths that duplicate paths are not explored twice.

    """
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur_index: int, subset: List[int]) -> None:
            res.append(subset[:])

            for index in range(cur_index, len(nums)):
                if index > cur_index and nums[index - 1] == nums[index]:
                    continue

                subset.append(nums[index])
                dfs(index + 1, subset)
                subset.pop()

        nums.sort()
        dfs(0, [])

        return res


@pytest.mark.parametrize(
    "nums, expected_result",
    (
        ([1, 2, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),
        ([1,2,3], [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]),
        ([0], [[], [0]]),
    )
)
def test_subsets_with_dup(nums, expected_result):
    assert Solution().subsetsWithDup(nums) == expected_result
