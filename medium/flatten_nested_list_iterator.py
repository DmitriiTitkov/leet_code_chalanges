"""
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with
the nested list nestedList. int next() Returns the next integer in the nested
list. boolean hasNext() Returns true if there are still some integers in the
nested list and false otherwise. Your code will be tested with the following
pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
If res matches the expected flattened list, then your code will be judged as
correct.

Example 1:
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order
of elements returned by next should be: [1,1,2,1,1].

Example 2:
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order
of elements returned by next should be: [1,4,6].

Constraints:
1 <= nestedList.length <= 500
The values of the integers in the nested list is in the range [-106, 106].
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from __future__ import annotations


class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> [NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
#        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self._iterator = self.__next(nestedList)
        try:
            self.next_nested_int = next(self._iterator)
        except StopIteration:
            self.next_nested_int = None

    def __next(self, nestedList: [NestedInteger]):
        for nested_item in nestedList:
            if nested_item.isInteger():
                yield nested_item.getInteger()
            else:
                for item in self.__next(nested_item.getList()):
                    yield item

    def next(self) -> int:
        res = self.next_nested_int
        try:
            self.next_nested_int = next(self._iterator)
        except StopIteration:
            self.next_nested_int = None
        return res

    def hasNext(self) -> bool:
        return self.next_nested_int is not None

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
