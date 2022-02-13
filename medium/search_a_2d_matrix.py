"""
https://leetcode.com/problems/search-a-2d-matrix/
Write an efficient algorithm that searches for a value target in an m x n
integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
from typing import List

import pytest


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        The idea is to use binary search twice to find row and then to find
        column.
        Time: O(lognm)
        Space: O(1)
        """
        # search of row
        l = 0
        r = len(matrix) - 1

        while l < r:
            mid = (l + r) // 2  # 1
            if matrix[mid][0] == target:
                return True

            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1

        # search column
        row = l if matrix[l][0] <= target else l - 1

        l, r = 0, len(matrix[row]) - 1
        while l <= r:

            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True

            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False


@pytest.mark.parametrize(
    "matrix,target,expected_result", (
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
        ([[1]], 1, True),
        ([[1], [3]], 3, True),
    )
)
def test_search(matrix, target, expected_result):
    assert Solution().searchMatrix(matrix, target) == expected_result
