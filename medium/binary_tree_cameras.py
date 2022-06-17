
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


CAMERA = 0
WATCHED = 1
NON_WATCHED = 2


class Solution:
    """
    Go bottom up and skip leave nodes to reduce amount of cameras.
    Time: O(n)
    Space: O(h)

    n - number of nodes
    h - height of the tree
    """
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.camera_counter = 0

        def set_cameras(root: Optional[TreeNode]) -> int:
            if root is None:
                return WATCHED

            left_state = set_cameras(root.left)
            right_state = set_cameras(root.right)

            if left_state == NON_WATCHED or right_state == NON_WATCHED:
                self.camera_counter += 1
                return CAMERA

            if left_state == CAMERA or right_state == CAMERA:
                return WATCHED

            return NON_WATCHED

        state = set_cameras(root)
        return self.camera_counter if state <= 1 else self.camera_counter +1
