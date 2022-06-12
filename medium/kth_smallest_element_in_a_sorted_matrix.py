"""
Given an n x n matrix where each of the rows and columns is sorted in ascending
order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth
distinct element.

You must find a solution with a memory complexity better than O(n2).

Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the
8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in
non-decreasing order.
1 <= k <= n2


Follow up:

Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.
"""
import heapq
from dataclasses import dataclass, field
from typing import List, Any


@dataclass(order=True, slots=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)


class Solution:
    """
    User priority queue to get proper number.
    Time: O(n^2)
    Space: O(n^2)
    n - is the length of row(or col)
    """
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        length = len(matrix)
        heap = []
        heapq.heappush(heap, PrioritizedItem(matrix[0][0], (0, 0)))
        queued = set((0, 0))

        for i in range(k):
            p_item = heapq.heappop(heap)
            row, col = p_item.item

            if row < length - 1 and (row + 1, col) not in queued:
                heapq.heappush(heap, PrioritizedItem(matrix[row + 1][col], (row + 1, col)))
                queued.add((row + 1, col))

            if col < length - 1 and (row, col + 1) not in queued:
                heapq.heappush(heap, PrioritizedItem(matrix[row][col + 1], (row, col + 1)))
                queued.add((row, col + 1))

        return matrix[row][col]

# TODO: Add test
# TODO: Find constant time solution
