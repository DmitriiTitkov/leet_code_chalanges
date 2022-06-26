"""
Given a binary tree, determine if it is height-balanced. For this problem, a
height-balanced binary tree is defined as: a binary tree in which the left and
right subtrees of every node differ in height by no more than 1.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""

from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Use recursive function that returns tuple. First is boolean flag that
    indicates whether subtree is balance second is int that represents maximum
    subtree length.
    Time: O(n)
    Space: O(h)
    n - number of nodes
    h - height of the tree
    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def is_balanced_recursive(root) -> Tuple[bool, int]:
            if root is None:
                return True, 0

            left_balanced, left_length = is_balanced_recursive(root.left)
            right_balanced, right_length = is_balanced_recursive(root.right)
            balance = True

            if not (left_balanced and right_balanced):
                balance = False

            if abs(left_length - right_length) > 1:
                balance = False

            return balance, max(left_length + 1, right_length + 1)

        return is_balanced_recursive(root)[0]
