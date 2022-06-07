"""
https://leetcode.com/problems/sort-list/
Given the head of a linked list, return the list after sorting it in ascending
order.

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory
(i.e. constant space)?
"""
from typing import Tuple, Optional

import pytest

from test_tools.linked_lists import ListNode, list_to_linked_list, linked_list_to_list


class Solution:
    """
    Merge Sort
    Time: O(n log n)
    Space: O(logn)
    """
    def split(self, head: ListNode) -> Tuple[ListNode, ListNode]:
        length = 0

        node = head
        while node:
            length += 1
            node = node.next

        mid = head
        for i in range((length - 1) // 2):
            mid = mid.next

        l1 = head
        l2 = mid.next
        mid.next = None
        return l1, l2

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged = ListNode(0)
        tail = merged

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        else:
            tail.next = l2

        return merged.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head

        l1, l2 = self.split(head)  # O(n)
        return self.merge(self.sortList(l1), self.sortList(l2))  # O(n * logn)


@pytest.mark.parametrize(
    "input_list,expected_output", (
        ([4, 2, 1, 3], [1, 2, 3, 4]),
        ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]),
        ([], []),
    ),

)
def test_sort_list(input_list, expected_output):
    ll = list_to_linked_list(input_list)
    res = Solution().sortList(ll)
    assert linked_list_to_list(res) == expected_output
