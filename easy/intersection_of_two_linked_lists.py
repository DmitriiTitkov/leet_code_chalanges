"""

"""
from typing import Optional

from test_tools.linked_lists import ListNode


class Solution:
    """
    Measure the length of lists and move pointers to the same position.
    Time: O(n+m)
    Space: O(1)
    where:
        n - length of first list
        m - length of second list
    """
    def get_llist_length(self, head: ListNode) -> int:
        length = 0
        while head:
            head = head.next
            length += 1

        return length

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        list_a_lenght = self.get_llist_length(headA)
        list_b_lenght = self.get_llist_length(headB)

        long_list = headA if list_a_lenght >= list_b_lenght else headB
        short_list = headA if list_a_lenght < list_b_lenght else headB

        for i in range(abs(list_a_lenght - list_b_lenght)):
            long_list = long_list.next

        while long_list and short_list:
            if long_list is short_list:
                return long_list

            long_list = long_list.next
            short_list = short_list.next

        return None

