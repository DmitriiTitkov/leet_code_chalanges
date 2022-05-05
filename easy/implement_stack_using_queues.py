from collections import deque


class MyStack:
    """
    Time: O(n) pop
          O(1) push

    """
    def __init__(self):
        self.primary_q = deque()
        self.secondary_q = deque()
        self.top_ = None

    def push(self, x: int) -> None:
        self.primary_q.appendleft(x)
        self.top_ = x

    def pop(self) -> int:
        last_item = None
        while self.primary_q:
            last_item = self.primary_q.pop()
            if len(self.primary_q) > 0:
                self.top_ = last_item
                self.secondary_q.appendleft(last_item)

        self.primary_q, self.secondary_q = self.secondary_q, self.primary_q

        return last_item

    def top(self) -> int:
        return self.top_

    def empty(self) -> bool:
        return len(self.primary_q) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()