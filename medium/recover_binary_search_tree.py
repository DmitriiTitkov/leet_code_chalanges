"""
You are given the root of a binary search tree (BST), where the values of
exactly two nodes of the tree were swapped by mistake. Recover the tree without
changing its structure.

Example 1:
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3
makes the BST valid.

Example 2:
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2
and 3 makes the BST valid.

Constraints:
The number of nodes in the tree is in the range [2, 1000].
-231 <= Node.val <= 231 - 1


Follow up: A solution using O(n) space is pretty straight-forward. Could you
devise a constant O(1) space solution?
"""

# Definition for a binary tree node.
from typing import Optional

import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Use non local variables to keep track of previous node during in-order
    traversal.
    Time: O(n) where n number of nodes
    Space: O(1)
    """
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first: Optional[TreeNode] = None
        second: Optional[TreeNode] = None

        previous = TreeNode(float("-inf"))

        def dfs(node):
            nonlocal previous, first, second

            if node.left:
                dfs(node.left)

            if node.val < previous.val and first is None:
                first = previous
                second = node
            elif node.val < previous.val:
                second = node

            previous = node

            if node.right:
                dfs(node.right)

        dfs(root)

        # swap nodes
        first.val, second.val = second.val, first.val


@pytest.mark.parametrize(
    "input_tree,expected_result",
    (
        (
            TreeNode(1,left=TreeNode(3, right=TreeNode(2))),
            TreeNode(3,left=TreeNode(1, right=TreeNode(2))),
        ),
        (
            TreeNode(3, left=TreeNode(1), right=TreeNode(4, left=TreeNode(2))),
            TreeNode(2, left=TreeNode(1), right=TreeNode(4, left=TreeNode(3))),
        ),
    )
)
def test_recover_tree(input_tree, expected_result):
    # TODO: Add tools for tree comparison
    pass
