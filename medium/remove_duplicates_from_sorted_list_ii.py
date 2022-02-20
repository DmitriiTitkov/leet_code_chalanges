"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
Given the head of a sorted linked list, delete all nodes that have duplicate
numbers, leaving only distinct numbers from the original list. Return the
linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""


from typing import Optional

import pytest

from test_tools.linked_lists import ListNode, list_to_linked_list, linked_list_to_list


class Solution:
    """
    Iterate over linked list skipping all repeating nodes using inner loop.
    Time: O(n)
    Space: O(1)
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(val=0, next=head)
        l = r = head

        while r and l:
            r = r.next
            repeating = False

            while r and r.next and r.val == r.next.val:
                repeating = True
                r = r.next

            if repeating:
                continue

            l.next = r
            l = l.next

        return head.next


@pytest.mark.parametrize(
    "test_list,expected_output",
    (
        ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
        ([1, 1, 1, 1, 2, 3], [2, 3]),
        ([1, 2, 3, 3, 3, 3], [1, 2]),
    )
)
def test_delete_duplicates(test_list, expected_output):
    linked_test_list = list_to_linked_list(test_list)
    res = Solution().deleteDuplicates(linked_test_list)
    output = linked_list_to_list(res)

    assert output == expected_output
