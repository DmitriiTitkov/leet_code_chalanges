"""
There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where
prerequisites[i] = [ai, bi] indicates that you must take course bi first if you
want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you
should also have finished course 1. So it is impossible.

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""
from collections import defaultdict, deque
from typing import List, Set

import pytest


class Solution:
    """
    Topological sort. Find node with 0 in-degree(edges directed to the node)
    remove it and remove all the edges that start from it.
    Time: O(E + V) amount of edges + amount of vertices
    Space: O(E + E + E) graph, indegree and queue
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        course_graph: List[Set[int]] = [set() for _ in range(numCourses)]
        indegrees = [0] * numCourses
        queue = deque()
        courses_taken = 0

        for course, dep in prerequisites:
            if course == dep:
                return False
            course_graph[dep].add(course)
            indegrees[course] += 1

        for vertex, indeg in enumerate(indegrees):
            if indeg == 0:
                queue.appendleft(vertex)

        while queue:
            vertex = queue.pop()
            courses_taken += 1
            for next_vert in course_graph[vertex]:
                indegrees[next_vert] -= 1

                if indegrees[next_vert] == 0:
                    queue.appendleft(next_vert)

        return courses_taken >= numCourses


@pytest.mark.parametrize(
    "numCourses,prerequisites,expected_output",
    (
        (2, [[1, 0]], True),
        (3, [[1,0],[1,2],[0,1]], False),
    )
)
def test_can_finish(numCourses, prerequisites, expected_output):
    assert Solution().canFinish(numCourses,prerequisites) == expected_output
