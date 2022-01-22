from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked_list(input_list: List[int]) -> Optional[ListNode]:
    """Simple utility function to convert list to linked_list."""
    head = ListNode()
    prev = head

    for item in input_list:
        prev.next = ListNode(item)
        prev = prev.next

    return head.next


def linked_list_to_list(head: ListNode) -> List[int]:
    """Simple utility function to convert linked list to list."""
    res = []

    while head:
        res.append(head.val)
        head = head.next

    return res

