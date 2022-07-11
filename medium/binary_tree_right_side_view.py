"""
Given the root of a binary tree, imagine yourself standing on the right side
of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""


# Definition for a binary tree node.
import collections
from typing import List, Optional

import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Level order traversal trcking previous value
    Time: O(n)
    Space: O(n)
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return root

        queue = collections.deque()
        queue.appendleft((root, 0))
        previous_num = None
        previous_lvl = 0
        right_view = []

        while queue:
            node, lvl = queue.pop()

            if lvl != previous_lvl:
                right_view.append(previous_num)

            previous_num = node.val
            previous_lvl = lvl

            if node.left:
                queue.appendleft((node.left, lvl + 1))
            if node.right:
                queue.appendleft((node.right, lvl + 1))

        right_view.append(previous_num)

        return right_view

