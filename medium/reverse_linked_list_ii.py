"""
Given the head of a singly linked list and two integers left and right where
left <= right, reverse the nodes of the list from position left to position
right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

Follow up: Could you do it in one pass?
"""

from typing import Optional

import pytest

from test_tools.linked_lists import ListNode, list_to_linked_list, linked_list_to_list


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Reverse only part between 'right-left' and change right left pointers.
        As it's single linked list we need to remember a node before left and
        use dummy node in front of head in case 'left==head'

        Time: O(n)
        Space: O(1)
        """
        pre_head = ListNode(0, next=head)
        before_left = None
        prev = None
        curr = pre_head
        for _ in range(left):
            before_left = curr
            curr = curr.next

        for _ in range(right-left+1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        left_node = before_left.next
        before_left.next = prev
        left_node.next = temp

        return pre_head.next


@pytest.mark.parametrize(
    "input_list,left,right,expected_list",
    (
        ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
        ([5], 1, 1, [5]),
        ([3,5], 1, 2, [5,3]),
        ([1,2,3,4], 1, 4, [4,3,2,1]),
    )
)
def test_reverse_list(input_list, left, right, expected_list):
    input_ll = list_to_linked_list(input_list)
    reversed_list = Solution().reverseBetween(input_ll, left, right)

    assert linked_list_to_list(reversed_list) == expected_list
