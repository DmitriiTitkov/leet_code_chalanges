"""
(This problem is an interactive problem.)

Each ship is located at an integer point on the sea represented by a cartesian
plane, and each integer point may contain at most 1 ship.

You have a function Sea.hasShips(topRight, bottomLeft) which takes two points
as arguments and returns true If there is at least one ship in the rectangle
represented by the two points, including on the boundary.

Given two points: the top right and bottom left corners of a rectangle, return
the number of ships present in that rectangle. It is guaranteed that there are
at most 10 ships in that rectangle.

Submissions making more than 400 calls to hasShips will be judged Wrong Answer.
Also, any solutions that attempt to circumvent the judge will result in
disqualification.

Example :
Input:
ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
Output: 3
Explanation: From [0,0] to [4,4] we can count 3 ships within the range.

Example 2:
Input: ans = [[1,1],[2,2],[3,3]], topRight = [1000,1000], bottomLeft = [0,0]
Output: 3

Constraints:
On the input ships is only given to initialize the map internally. You must
solve this problem "blindfolded". In other words, you must find the answer
using the given hasShips API, without knowing the ships position.
0 <= bottomLeft[0] <= topRight[0] <= 1000
0 <= bottomLeft[1] <= topRight[1] <= 1000
topRight != bottomLeft
"""


# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
from collections import deque


class Sea:
   def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution:
    """Divide and conquer
    TODO: Analise Time & Space Complexity
    """
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        queue = deque()
        queue.appendleft((topRight, bottomLeft))

        ship_count = 0

        while queue:
            top_right, bottom_left = queue.pop()
            if not sea.hasShips(top_right, bottom_left):
                continue
            if top_right.x == bottom_left.x and top_right.y == bottom_left.y:
                ship_count += 1
                continue

            if top_right.x - bottom_left.x < top_right.y - bottom_left.y:
                mid_y = (top_right.y + bottom_left.y) // 2
                queue.appendleft(
                    (top_right, Point(bottom_left.x, mid_y + 1))
                )
                queue.appendleft(
                    (Point(top_right.x, mid_y), bottom_left)
                )

            else:
                mid_x = (top_right.x + bottom_left.x) // 2
                queue.appendleft(
                    (top_right, Point(mid_x + 1, bottom_left.y))
                )
                queue.appendleft(
                    (Point(mid_x, top_right.y), bottom_left)
                )

        return ship_count

