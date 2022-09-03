"""
Return all non-negative integers of length n such that the absolute difference
between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros. For example,
01 has one leading zero and is invalid.

You may return the answer in any order.

Example 1:
Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Example 2:
Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

Constraints:

2 <= n <= 9
0 <= k <= 9
"""
from typing import List

import pytest


class Solution:
    """
    Time: O(2^N)
    Space: O(2^N) - O(N) without response
    """
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        nums = []

        def generate_nums(num: List[int], n: int, k: int) -> None:
            if n == 0:
                combined_num = 0
                for i, digit in enumerate(num):
                    pos = len(num) - i - 1
                    combined_num += digit * 10 ** pos

                nums.append(combined_num)
                return

            if num[-1] - k >= 0:
                num.append(num[-1] - k)
                generate_nums(num, n - 1, k)
                num.pop()

            if num[-1] + k < 10 and k != 0:
                num.append(num[-1] + k)
                generate_nums(num, n - 1, k)
                num.pop()

        for i in range(1, 10):
            generate_nums([i], n - 1, k)

        return nums


@pytest.mark.parametrize(
    "n,k,expected_output", (
        (3, 7, [181, 292, 707, 818, 929]),
        (2, 1, [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]),
    )
)
def test_nums_same_consec_diff(n, k, expected_output):
    assert Solution().numsSameConsecDiff(n, k) == expected_output
