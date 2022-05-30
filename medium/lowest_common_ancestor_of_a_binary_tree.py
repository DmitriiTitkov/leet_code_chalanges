"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
in the tree. According to the definition of LCA on Wikipedia: “The lowest
common ancestor is defined between two nodes p and q as the lowest node in T
that has both p and q as descendants (where we allow a node to be a descendant
of itself).”

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of
itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""


# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Traverse the tree twice an compare paths
    Time: O(n)
    Space: O(n) - worst case for skewed tree

    n - number of nodes in the tree
    """
    def find_node_path(
            self,
            root: 'TreeNode',
            target: 'TreeNode',
            cur_path: Optional[List['TreeNode']] = None,
    ) -> List['TreeNode']:
        if cur_path is None:
            cur_path = []

        cur_path.append(root)

        if root.val == target.val:
            return cur_path

        if root.left:
            path = self.find_node_path(root.left, target, cur_path)
            if path is not None:
                return path

        if root.right:
            path = self.find_node_path(root.right, target, cur_path)
            if path is not None:
                return path

        cur_path.pop()

        return None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_to_p = self.find_node_path(root, p)
        path_to_q = self.find_node_path(root, q)

        lca = root
        shortest_path = min(len(path_to_p), len(path_to_q))
        for i in range(shortest_path):
            if path_to_p[i].val == path_to_q[i].val:
                lca = path_to_p[i]

        return lca
