from collections import Counter
from typing import Optional, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    DFS Solution.
    Time: O(N) - visit each node at least once
    Space: O(N) - worst case scenario for recursion
    """
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], cur_lvl: int, counter: Dict[int, int]) -> None:
            counter[cur_lvl] += node.val
            if node.left:
                dfs(node.left, cur_lvl + 1, counter)
            if node.right:
                dfs(node.right, cur_lvl + 1, counter)

        lvl_sum = Counter()
        dfs(root, 0, lvl_sum)
        deepest_lvl = max(lvl_sum.keys())
        return lvl_sum[deepest_lvl]
