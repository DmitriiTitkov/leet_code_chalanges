"""
Given the root of a binary tree and an integer targetSum, return the number of
paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go
downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Constraints:
The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
"""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Use two layers of DFS one to traverse the Tree and another to find the Sum
    Time: O(N^2) N for traversal and N for dfs for each node
    Space: O(h) as at any moment we will have two recursion stacks in memory but
    second stack will start at some subtree element

    """
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.traverse_tree(root, targetSum)

    def traverse_tree(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0

        return sum([
            self.find_path_count(root, targetSum),
            self.traverse_tree(root.left, targetSum),
            self.traverse_tree(root.right, targetSum),
        ])

    def find_path_count(self, root: Optional[TreeNode], targetSum: int, curSum: int = 0) -> int:
        if root is None:
            return 0

        current_path_count = 0
        curSum += root.val
        if targetSum == curSum:
            current_path_count = 1

        return sum([
            current_path_count,
            self.find_path_count(root.left, targetSum, curSum),
            self.find_path_count(root.right, targetSum, curSum),
        ])

