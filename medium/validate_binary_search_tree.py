"""
Given the root of a binary tree, determine if it is a valid binary search tree
(BST). A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""


# Definition for a binary tree node.
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Check the min and max node of subtree during backtracking.
    Time: O(n)
    Space: O(1)
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root: Optional[TreeNode]) -> Tuple[int, int]:
            min_val = max_val = root.val

            if root.left is not None:
                min_subtree_val, max_subtree_val = dfs(root.left)
                if max_subtree_val >= root.val:
                    raise ValueError("Not A BST")
                min_val = min_subtree_val

            if root.right is not None:
                min_subtree_val, max_subtree_val = dfs(root.right)
                if min_subtree_val <= root.val:
                    raise ValueError("Not A BST")
                max_val = max_subtree_val

            return min_val, max_val

        try:
            dfs(root)
            return True
        except ValueError:
            return False
