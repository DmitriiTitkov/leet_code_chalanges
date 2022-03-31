"""
https://leetcode.com/problems/all-paths-from-source-to-target/
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find
all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit
from node i (i.e., there is a directed edge from node i to node graph[i][j]).

Example 1:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Example 2:
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

Constraints:
n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
All the elements of graph[i] are unique.
The input graph is guaranteed to be a DAG.
"""
from typing import List

import pytest


class Solution:
    """
    DFS Search, complexity is not straightforward

    """
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def dfs(graph, current: int, path: List, all_paths: List) -> List[List[int]]:
            path.append(current)

            if current == len(graph) - 1:
                all_paths.append(path)

            for next_node in graph[current]:
                dfs(graph, next_node, path.copy(), all_paths)

            return all_paths

        return dfs(graph, 0, [], [])


class Solution2:
    """
    DFS iterative

    """
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        stack = [(0, [0])]
        res = []
        cur_res = []

        while stack:
            cur_node, cur_path = stack.pop()

            if cur_node == len(graph) -1:
                res.append(cur_path)
            else:
                for next_node in graph[cur_node]:
                    stack.append((next_node, cur_path.append(next_node)))


        return res


@pytest.mark.parametrize(
    "graph,expected_result",
    (
        (
            [[1, 2], [3], [3], []],
            [[0, 1, 3], [0, 2, 3]],
        ),
        (
            [[4, 3, 1], [3, 2, 4], [3], [4], []],
            [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]],
        ),
    )

)
def test_all_paths(graph,expected_result):
    assert Solution().allPathsSourceTarget(graph) == expected_result
