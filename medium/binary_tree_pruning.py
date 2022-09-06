"""
Given the root of a binary tree, return the same tree where every subtree
(of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.

Example 1:
Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation:
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.

Example 2:
Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]

Example 3:
Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]

Constraints:
The number of nodes in the tree is in the range [1, 200].
Node.val is either 0 or 1.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Use DFS and remove subtrees with sum equals to 0
    Time: O(n)
    Space: O(h)
    """
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def prune_zeros_rec(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            sum_left = prune_zeros_rec(root.left)
            if sum_left == 0:
                root.left = None
            sum_right = prune_zeros_rec(root.right)
            if sum_right == 0:
                root.right = None

            return sum_left + sum_right + root.val

        tree_sum = prune_zeros_rec(root)
        if tree_sum == 0:
            return None
        return root
