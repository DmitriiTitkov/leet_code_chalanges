"""
https://leetcode.com/problems/critical-connections-in-a-network/
There are n servers numbered from 0 to n - 1 connected by undirected
server-to-server connections forming a network where connections[i] = [ai, bi]
represents a connection between servers ai and bi. Any server can reach other
servers directly or indirectly through the network.
A critical connection is a connection that, if removed, will make some servers
unable to reach some other server.
Return all critical connections in the network in any order.

Example 1:
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

Example 2:
Input: n = 2, connections = [[0,1]]
Output: [[0,1]]

Constraints:
2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.
"""
from collections import defaultdict
from typing import List

import pytest


class Solution:
    """Detect cycles in graph by comparing current stack depth(time) with the
    depth(time) it was initially accessed. Then lowest found access time
    propagates through dfs stack. If it's greater than current time it means
    that cycle has not been found and edge represents 'critical connection'

    Time: O(E+V) all nodes and all edges
    Space: O(E+V)
    """
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        low = [-1] * n
        parent = [-1] * n
        adj_nodes = defaultdict(list)

        crit_connections = []

        for src, dest in connections:
            adj_nodes[src].append(dest)
            adj_nodes[dest].append(src)

        def dfs(node, time, prev):
            if low[node] != -1:
                return low[node]

            if parent[node] == -1:
                parent[node] = prev

            low[node] = time

            for dest in adj_nodes[node]:
                if parent[node] != dest:
                    lowest_reachable = dfs(dest, time + 1, node)
                    low[node] = min(low[node], lowest_reachable)

                    if lowest_reachable > time:
                        crit_connections.append([node, dest])

            return low[node]

        dfs(0, 0, -1)
        return crit_connections


@pytest.mark.parametrize(
    "n,connections,expected_output", (
        (
            4, [[0, 1], [1, 2], [2, 0], [1, 3]], [[1, 3]]
        ),
        (
            8,
            [[6, 1], [1, 2], [2, 3], [3, 4], [4, 1], [4, 5], [5, 6], [1, 0], [0, 7]],
            [[0, 1], [0, 7]],
        ),
    )
)
def test_set_zeroes(n, connections, expected_output):
    assert Solution().criticalConnections(n, connections) == expected_output
