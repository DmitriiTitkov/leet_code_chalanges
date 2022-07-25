"""
Given the head of a linked list, return the node where the cycle begins. If
there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be
reached again by continuously following the next pointer. Internally, pos is
used to denote the index of the node that tail's next pointer is connected to
(0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a
parameter.
Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the
second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the
first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.


Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""
from typing import Optional

import pytest

from medium.lru_cache import ListNode


class Solution:
    """
    Use two nodes one is doing double steps other is doing single steps. When
    they meet use intersection and head to iterate until the cycle node.
    Time: O(n)
    Space: O(1)
    n - number of nodes
    """
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return

        fast = slow = head

        while True:
            if fast.next is None or fast.next.next is None:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                break

        while head is not slow:
            head = head.next
            slow = slow.next

        return head
