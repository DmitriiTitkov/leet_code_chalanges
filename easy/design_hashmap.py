"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If
the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1
if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains
the mapping for the key.

Example 1:
Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]


Constraints:
0 <= key, value <= 106
At most 104 calls will be made to put, get, and remove.
"""


class ListNode:
    def __init__(self, key: int, val: int, next_node=None):
        self.key = key
        self.val = val
        self.next = next_node


class MyHashMap:
    """Use Linked list to store values in the buckets"""
    def __init__(self):
        self.size = 5031
        self.buckets = [ListNode(None, None)] * self.size

    def _hash(self, key: int):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        pos = self._hash(key)

        node = prev_node = self.buckets[pos]
        while node:
            if node.key == key:
                node.val = value
                return

            prev_node = node
            node = node.next

        prev_node.next = ListNode(key, value)

    def get(self, key: int) -> int:
        pos = self._hash(key)

        node = self.buckets[pos]
        while node:
            if node.key == key:
                return node.val
            node = node.next

        return -1

    def remove(self, key: int) -> None:
        pos = self._hash(key)

        node = prev_node = self.buckets[pos]
        while node:
            if node.key == key:
                prev_node.next = node.next

            prev_node = node
            node = node.next
