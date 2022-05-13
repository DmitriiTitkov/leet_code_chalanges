"""
Given the root of a binary tree, return the level order traversal of its nodes'
values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    BFS solution to show all the nodes
    Time: O(N)  N- amount of the nodes
    Space: O(2**h) h - tree height
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque()
        queue.appendleft((root, 0))
        prev_lvl = 0
        level_order_traversal = [[]]

        while queue:
            node, lvl = queue.pop()

            if lvl != prev_lvl:
                level_order_traversal.append([])
                prev_lvl = lvl

            level_order_traversal[lvl].append(node.val)

            if node.left:
                queue.appendleft((node.left, lvl + 1))
            if node.right:
                queue.appendleft((node.right, lvl + 1))

        return level_order_traversal
