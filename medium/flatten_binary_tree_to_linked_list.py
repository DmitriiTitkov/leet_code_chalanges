from typing import Optional, Tuple

from medium.construct_binary_tree_from_preorder_and_inorder_traversal import TreeNode


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Flatten left and right subtree recursively.
    Time: O(n)
    Space: O(log n)

    """
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def linarize(root: Optional[TreeNode]) -> Optional[Tuple[TreeNode, TreeNode]]:
            if root is None:
                return None

            if root.left is None and root.right is None:
                return root, root

            # linerize left
            left_nodes = linarize(root.left)
            if left_nodes is None:
                left_nodes = (root, root)

            first_left, last_left = left_nodes

            # linerize right
            right_nodes = linarize(root.right)
            if right_nodes is None:
                right_nodes = (None, None)

            first_right, last_right = right_nodes

            root.left = None
            root.right = first_left
            last_left.right = first_right

            last_node = last_right if last_right is not None else last_left

            return root, last_node

        linarize(root)
