"""
Given two binary trees original and cloned and given a reference to a node
target in the original tree. The cloned tree is a copy of the original tree.
Return a reference to the same node in the cloned tree. Note that you are not
allowed to change any of the two trees or the target node and the answer must
be a reference to a node in the cloned tree.

Example 1:
Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. The
target node is a green node from the original tree. The answer is the yellow
node from the cloned tree.

Example 2:
Input: tree = [7], target =  7
Output: 7

Example 3:
Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
Output: 4

Constraints:
The number of nodes in the tree is in the range [1, 104].
The values of the nodes of the tree are unique.
target node is a node from the original tree and is not null.


Follow up: Could you solve the problem if repeated values on the tree are allowed?
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """DFS Solution with" breadcrumbs
    Time: O(n)
    Space: O(logn)
    """
    def dfs(self, tree: TreeNode, target: TreeNode, path: List[int]) -> List[int]:
        path.append(tree.val)
        if tree is target:
            return path

        for child in (tree.left, tree.right):
            if child is not None:
                res = self.dfs(child, target, path)
                if res is not None:
                    return res
        path.pop()
        return None

    def traverse_breadcrumbs(self, tree: TreeNode, path: List[int]) -> TreeNode:
        for i in range(1, len(path)):
            num = path[i]
            if tree.left is not None and tree.left.val == num:
                tree = tree.left
            else:
                tree = tree.right

        return tree


    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        path = self.dfs(original, target, [])
        return self.traverse_breadcrumbs(cloned, path)
