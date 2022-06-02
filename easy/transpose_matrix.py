"""
Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal,
switching the matrix's row and column indices.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109
"""
from typing import List


class Solution:
    """Transpose matrix to pre allocated 2d array
    Time: O(m * n)
    Space: O(m * n)
    """
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row_num = len(matrix)
        col_num = len(matrix[0])

        transposed_matrix = [[0] * row_num for _ in range(col_num)]

        for row in range(row_num):
            for col in range(col_num):
                transposed_matrix[col][row] = matrix[row][col]

        return transposed_matrix
