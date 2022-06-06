"""
Given the root of a binary tree, return the zigzag level order traversal of
its nodes' values. (i.e., from left to right, then right to left for the next
level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Use two stacks for current lvl and next.
    Time: O(n)
    Space: O(n) - as we need to store the result
    """
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return

        curr_lvl_stack = [(root, 0)]
        next_lvl_stack = []

        zig_zag_traversal = [[]]

        while curr_lvl_stack or next_lvl_stack:
            if not curr_lvl_stack:
                curr_lvl_stack = next_lvl_stack
                next_lvl_stack = []
                zig_zag_traversal.append([])

            node, lvl = curr_lvl_stack.pop()

            if node.right and lvl % 2 != 0:
                next_lvl_stack.append((node.right, lvl+1))

            if node.left:
                next_lvl_stack.append((node.left, lvl+1))

            if node.right and lvl % 2 == 0:
                next_lvl_stack.append((node.right, lvl+1))

            zig_zag_traversal[lvl].append(node.val)

        return zig_zag_traversal
