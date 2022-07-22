"""
Given the head of a linked list and a value x, partition it such that all nodes
less than x come before nodes greater than or equal to x. You should preserve
the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]


Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""

from typing import Optional

import pytest

from test_tools.linked_lists import ListNode, list_to_linked_list, linked_list_to_list


class Solution:
    """
    Repoint references to two linked lists and then connect them
    Time: O(n)
    Space: O(1)
    """
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_head = ListNode(0)
        left_tail = left_head
        right_head = ListNode(0)
        right_tail = right_head

        while head:
            if head.val < x:
                left_tail.next = head
                left_tail = left_tail.next
            else:
                right_tail.next = head
                right_tail = right_tail.next

            head = head.next

        left_tail.next = right_head.next
        right_tail.next = None
        return left_head.next


@pytest.mark.parametrize(
    "input_list,x,expected_output", (
        ([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5]),
        ([2, 1], 2, [1, 2]),
    ),
)
def test_partition(input_list, x, expected_output):
    head = list_to_linked_list(input_list)
    res = Solution().partition(head, x)

    assert linked_list_to_list(res) == expected_output
