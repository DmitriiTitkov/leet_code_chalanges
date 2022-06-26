"""
226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
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
    Iterative approach.
    Time: O(n)
    Space: O(h)
    n - number of nodes
    h - height of the tree
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        stack = [root]

        while stack:
            node = stack.pop()

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

            node.left, node.right = node.right, node.left

        return root


class Solution2:
    """
    Recursive approach.
    Time: O(n)
    Space: O(n)
    n - number of nodes
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert_tree_recursive(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if root is None:
                return root

            invert_tree_recursive(root.left)
            invert_tree_recursive(root.right)

            root.left, root.right = root.right, root.left
            return root

        return invert_tree_recursive(root)