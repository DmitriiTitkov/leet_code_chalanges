"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next
right node, the next pointer should be set to NULL.Initially, all next pointers
are set to NULL.

Example 1:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should
populate each next pointer to point to its next right node, just like in Figure
B. The serialized output is in level order as connected by the next pointers,
with '#' signifying the end of each level.

Example 2:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 6000].
-100 <= Node.val <= 100

Follow-up:
You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not
count as extra space for this problem.
"""
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """Level-order traversal using queue
            time: O(n)
            space: O(n)
        """
        queue = deque()
        if root is not None:
            queue.appendleft((root, 0))

        next_right_node = None
        last_depth = 0

        while queue:
            node, depth = queue.pop()

            if depth == last_depth:
                node.next = next_right_node

            if node.right is not None:
                queue.appendleft((node.right, depth+1))

            if node.left is not None:
                queue.appendleft((node.left, depth+1))

            next_right_node = node
            last_depth = depth

        return root


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        TODO: re-try time O(1) implementation
        time: O(n)
        space: O(1)
        """
        node  = root
        curr = dummy = Node(0)
        while node:
            curr.next = node.left
            if curr.next:
                curr = curr.next

            curr.next = node.right
            if curr.next:
                curr = curr.next

            node = node.next
            if not node:
                curr = dummy
                node = dummy.next

        return root




root = Solution().connect(
    Node(1, left=Node(2, left=Node(4), right=Node(5)), right=Node(3, right=Node(7)))
)

q = deque()
q.appendleft(root)
while q:
    node = q.pop()
    if node:
        print(f"{node.val} -> {node.next}")
        q.appendleft(node.left)
        q.appendleft(node.right)

