"""
Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.
A height-balanced binary tree is a binary tree in which the depth of the two
subtrees of every node never differs by more than one.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
"""
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Build bst recursively
    Time: O(n)
    Space: O(logn)

    n - len of nums array
    """
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_bst(nums: List[int], l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            mid = (l + r) // 2
            return TreeNode(
                val=nums[mid],
                left=build_bst(nums, l, mid - 1),
                right=build_bst(nums, mid + 1, r),
            )

        return build_bst(nums, 0, len(nums) - 1)
