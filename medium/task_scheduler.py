"""
Given a characters array tasks, representing the tasks a CPU needs to do, where
each letter represents a different task. Tasks could be done in any order. Each
task is done in one unit of time. For each unit of time, the CPU could complete
either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period
between two same tasks (the same letter in the array), that is that there must
be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all
the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation:
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

Constraints:
1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].
"""
import heapq
from collections import deque, Counter
from typing import List

import pytest


class Solution:
    """
    Use priority queue to track most frequent task. As soon as task is added to
    the schedule(counted) we place it into separate queue. It cannot be added
    again until n iterations passed.
    Time: O(n + k)
    Space: O(k)

    k - amount of tasks
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks).values()
        heap = list(map(lambda x: x * -1, counts))
        heapq.heapify(heap)
        queue = deque()

        cur_cpu_unit = 0

        while heap or queue:
            if queue and queue[-1][1] == cur_cpu_unit:
                heapq.heappush(heap, queue.pop()[0])

            if heap:
                count = heapq.heappop(heap) + 1
                if count < 0:
                    queue.appendleft((count, cur_cpu_unit + n + 1))

            cur_cpu_unit += 1

        return cur_cpu_unit


@pytest.mark.parametrize(
    "nums,n,expected_output", (
        (["A", "A", "A", "B", "B", "B"], 2, 8),
        (["A", "A", "A", "B", "B", "B"], 0, 6),
        (["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2, 16),
    )
)
def test_least_interval(nums, n, expected_output):
    assert Solution().leastInterval(nums, n) == expected_output
