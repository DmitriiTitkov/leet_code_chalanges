"""
https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/
Given the root of a binary tree, return the inorder traversal of its nodes'
values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import Optional, List

import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Simple recursive inorder traversal
    Time: O(n)
    Space: O(n)  # O(2n) as we need stack and response list
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            if root.left:
                res += self.inorderTraversal(root.left)

            res.append(root.val)

            if root.right:
                res += self.inorderTraversal(root.right)

        return res


class Solution2:
    """Simple iterative inorder traversal
    Time: O(n)
    Space: O(n)  # in average stack should not be bigger than O(logn)
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            res.append(root.val)
            root = root.right

        return res




@pytest.mark.parametrize(
    "solution", (Solution, Solution2),
)
@pytest.mark.parametrize(
    "root,expected_result",
    (
        # [1,null,2,3]
        (TreeNode(1, None, TreeNode(2, TreeNode(3))), [1,3,2]),
        # [1]
        (TreeNode(1), [1]),
        # [2,3,null,1]
        (TreeNode(2, TreeNode(3, TreeNode(1))), [1, 3, 2]),
    )
)
def test_inorder_traversal(solution, root, expected_result):
    assert solution().inorderTraversal(root) == expected_result
