"""
Given the root of a binary search tree, and an integer k, return the kth
smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104

Follow up: If the BST is modified often (i.e., we can do insert and delete
operations) and you need to find the kth smallest frequently, how would you
optimize?
"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Use instance attribute to track last visited node.
    Time: O(n)
    Space: O(n)
    n - number of nodes
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 0
        self.last_visited = None

        def traverse_inorder(root: Optional[TreeNode]):
            if root is None or self.counter == k:
                return

            traverse_inorder(root.left)

            if self.counter < k:
                self.counter += 1
                self.last_visited = root.val

            traverse_inorder(root.right)

        traverse_inorder(root)
        return self.last_visited


class Solution2:
    """Iterative search
    Time: O(n)
    Space: O(n)

    n - number of nodes
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val

            root = root.right
