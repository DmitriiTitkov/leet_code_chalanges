"""
You are given a network of n nodes, labeled from 1 to n. You are also given
times, a list of travel times as directed edges times[i] = (ui, vi, wi), where
ui is the source node, vi is the target node, and wi is the time it takes for a
signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the
n nodes to receive the signal. If it is impossible for all the n nodes to
receive the signal, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

Constraints:
1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""
from collections import defaultdict, deque
from typing import List

import pytest


class Solution:
    """BFS Solution.
    Time: O(N*E)
    Space: O(N*E)
    Where N number of nodes and E number of edges
    """
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodes = defaultdict(list)

        for edge in times:
            src, dest, weight = edge
            nodes[src].append((dest, weight))
            nodes[dest]

        if len(nodes) < n:
            return -1

        arrived_at = {}
        for node in nodes:
            arrived_at[node] = float('inf')

        queue = deque()
        queue.appendleft(k)
        arrived_at[k] = 0

        while queue:
            node = queue.pop()
            if not nodes[node]:
                continue

            for dest, weight in nodes[node]:
                arrvied_at_prev = arrived_at[dest]
                arrived_at[dest] = min(arrived_at[dest], arrived_at[node] + weight)

                if arrvied_at_prev != arrived_at[dest]:
                    queue.appendleft(dest)

        max_time = max(arrived_at.values())
        return max_time if max_time != float('inf') else -1



@pytest.mark.parametrize(
    "times,n,k,expected_output",
    (
        ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),
        ([[1, 2, 1]], 2, 1, 1),
        ([[1, 2, 1]], 2, 2, -1),
    ),
)
def test_network_delay_time(times, n, k, expected_output):
    assert Solution().networkDelayTime(times, n, k) == expected_output
