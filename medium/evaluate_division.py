"""
You are given an array of variable pairs equations and an array of real numbers
values, where equations[i] = [Ai, Bi] and values[i] represent the equation
Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth
query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined,
return -1.0.

Note: The input is always valid. You may assume that evaluating the queries
will not result in division by zero and that there is no contradiction.

Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0],
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0],
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5],
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

Constraints:
1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""
from collections import defaultdict
from functools import cache
from typing import List

import pytest


class Solution:
    """
    Treat equations as a graph and values as edge weights. DFS traverse graph to
    find results for queries.
    Time: O(e + (q * e))
    Space: O(4n) adj_list 2 refs + visited set set + cache

    e - amount of equations
    q - amount of queries
    """
    def calcEquation(
            self,
            equations: List[List[str]],
            values: List[float],
            queries: List[List[str]]
    ) -> List[float]:
        # create adjustancy list
        # space: O(n+n)
        adj_list = defaultdict(list)

        # time: O(E)
        for i, equation in enumerate(equations):
            adj_list[equation[0]].append((equation[1], values[i]))
            adj_list[equation[1]].append((equation[0], 1 / values[i]))

        # space: O(n)
        visited = set()

        # space: O(n)
        # time: O(N)
        @cache
        def find_path(cur: str, to: str) -> float:
            """DFS search"""
            if cur in adj_list and cur == to:
                return 1.0

            visited.add(cur)

            for vertex, edge in adj_list[cur]:
                if vertex in visited:
                    continue
                res = find_path(vertex, to)
                if res != -1.0:
                    visited.pop()
                    return res * edge

            visited.pop()
            return -1.0

        res = []
        for q in queries:
            res.append(find_path(q[0], q[1]))

        return res


@pytest.mark.parametrize(
    "equations,values,queries,expected_result",
    (
        (
            [["a", "b"], ["b", "c"], ["bc", "cd"]],
            [1.5, 2.5, 5.0],
            [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
            [3.75000, 0.40000, 5.00000, 0.20000],
        ),
        (
            [["a", "b"], ["b", "c"], ["bc", "cd"]],
            [1.5, 2.5, 5.0],
            [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
            [3.75000, 0.40000, 5.00000, 0.20000],
        ),
        (
            [["a", "b"]],
            [0.5],
            [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]],
            [0.50000, 2.00000, -1.00000, -1.00000],
        ),
    )

)
def test_eval_division(equations, values, queries, expected_result):
    assert Solution().calcEquation(equations, values, queries) == expected_result
