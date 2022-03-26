"""
https://leetcode.com/problems/subtree-of-another-tree/
Given the roots of two binary trees root and subRoot, return true if there is a
subtree of root with the same structure and node values of subRoot and false
otherwise. A subtree of a binary tree tree is a tree that consists of a node in
tree and all of this node's descendants. The tree tree could also be considered
as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Constraints:
The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_equal(root, root2) -> bool:
    if (root is None) ^ (root2 is None):
        return False

    if not root:
        return True

    if root.val != root2.val:
        return False

    if not is_equal(root.left, root2.left):
        return False
    if not is_equal(root.right, root2.right):
        return False

    return True


class Solution:
    """Naive approach, traverse through the tree and try to match subtree on
    every node.
    Time: O(n*m) Close looking trees will be checked until very last element
    Space: O(H) where H is height of the tree
    """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if is_equal(root, subRoot):
            return True

        if root.left and self.isSubtree(root.left, subRoot):
            return True

        if root.right and self.isSubtree(root.right, subRoot):
            return True

        return False
