"""
https://leetcode.com/problems/design-hashset/
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in
the HashSet, do nothing.


Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove",
"contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)


Constraints:

0 <= key <= 106
At most 104 calls will be made to add, remove, and contains.
"""
from typing import Optional


class ListNode:
    def __init__(self, val: Optional[int], next_node=None):
        self.val = val
        self.next_node = next_node


class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets = [ListNode(None) for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        node = self.buckets[self._hash(key)]
        while node.next_node:
            if node.val == key:
                return
            node = node.next_node

        if node.val != key:
            node.next_node = ListNode(key)

    def remove(self, key: int) -> None:
        node = prev_node = self.buckets[self._hash(key)]

        while node:
            if node.val == key:
                prev_node.next_node = node.next_node

            prev_node = node
            node = node.next_node

    def contains(self, key: int) -> bool:
        node = self.buckets[self._hash(key)]

        while node:
            if node.val == key:
                return True
            node = node.next_node

        return False
