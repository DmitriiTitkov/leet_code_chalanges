# Definition for a binary tree node.
from typing import Optional, List


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


class Solution:
    """Simple iterative inorder traversal
    Time: O(n)
    Space: O(n)  # O(2n) as we need stack and response list
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        fi = True

        while stack or fi:
            fi = False
            if root.left:
                stack.append(root)
                root = root.left
            else:
                res.append(root.val)
                if stack:
                    prev_root = stack.pop()
                    res.append(prev_root.val)
                    root = root.right

        return res






