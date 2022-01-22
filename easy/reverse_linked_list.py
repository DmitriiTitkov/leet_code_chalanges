"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""

# Definition for singly-linked list.
from typing import Optional, List

import pytest

from test_tools.linked_lists import ListNode, list_to_linked_list, linked_list_to_list


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Recursive list reversion"""

        def reverse_list(node: ListNode, next_node: ListNode):
            if not node:
                return next_node
            temp = node.next
            node.next = next_node
            return reverse_list(temp, node)

        return reverse_list(head, None)


class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Iterative list reversion"""

        cur = head
        prev = None

        while cur:
            temp = cur.next

            cur.next = prev
            prev = cur
            cur = temp

        return prev

@pytest.mark.parametrize(
    "cls", [Solution, Solution2]
)
@pytest.mark.parametrize(
    "input_list,expected_list",
    (
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
    )
)
def test_reverse_list(cls, input_list, expected_list):
    input_ll = list_to_linked_list(input_list)
    reversed_list = cls().reverseList(input_ll)

    assert linked_list_to_list(reversed_list) == expected_list
