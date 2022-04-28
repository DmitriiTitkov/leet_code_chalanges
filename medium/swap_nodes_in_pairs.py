"""
Given a linked list, swap every two adjacent nodes and return its head. Y
ou must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""
from typing import Optional

import pytest

from test_tools.linked_lists import ListNode, list_to_linked_list, linked_list_to_list


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)

        if not head or not head.next:
            return head

        prev_parent = dummy
        prev = head
        cur = head.next

        while cur is not None:
            prev_parent.next = cur
            prev.next = cur.next
            cur.next = prev

            prev_parent = prev
            prev = prev.next

            if prev:
                cur = prev.next
            else:
                cur = None

        return dummy.next


@pytest.mark.parametrize(
    "input_list,expected_list",
    (
        ([1, 2, 3, 4, 5], [2, 1, 4, 3, 5]),
        ([1, 2], [2, 1]),
        ([], []),
    )
)
def test_reverse_list(input_list, expected_list):
    input_ll = list_to_linked_list(input_list)
    reversed_list = Solution().swapPairs(input_ll)

    assert linked_list_to_list(reversed_list) == expected_list
