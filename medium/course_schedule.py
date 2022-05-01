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
from collections import defaultdict
from typing import List


class Solution:
    """
    Topological sort. Find node with 0 in-degree(edges directed to the node)
    remove it and remove all the edges that start from it.
    Time: O(n + p + (n * n))
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        dep_graph = defaultdict(set)

        # O(n)
        for num in range(numCourses):
            dep_graph[num]

        # O(p)
        for cur, dep in prerequisites:
            dep_graph[cur].add(dep)
            dep_graph[dep]

        num_of_taken = 0

        # O(n)
        while dep_graph or num_of_taken < numCourses:
            no_dep_node = None

            # O(n)
            for vertex, deps in dep_graph.items():
                if len(deps) == 0:
                    no_dep_node = vertex
                    break

            if no_dep_node == None:
                # Cycle found
                break

            num_of_taken += 1
            del dep_graph[no_dep_node]

            # O(n)
            for vertex in dep_graph:
                if no_dep_node in dep_graph[vertex]:
                    dep_graph[vertex].remove(no_dep_node)

        return num_of_taken >= numCourses



