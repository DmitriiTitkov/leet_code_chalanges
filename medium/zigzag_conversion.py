"""
https://leetcode.com/problems/zigzag-conversion/
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
rows like this: (you may want to display this pattern in a fixed font for better
legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number
of rows:

string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""
import pytest


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """The best solution I could come up by myself. Track direction and
        calculate next index based on the row number.
        Time: O(n)
        Space: O(n)
        """
        if numRows == 1:
            return s

        row = 1
        curr = 0

        res = []

        for i in range(len(s)):
            if curr >= len(s):
                row += 1
                curr = row-1

            if row == 1 or curr + 1 < numRows:
                direction = 1
            elif row == numRows:
                direction = 0
            else:
                direction = not direction

            res.append(s[curr])

            if direction:
                curr += ((numRows - row) * 2)
            else:
                curr += ((row-1)*2)

        return "".join(res)


class Solution2:
    def convert(self, s: str, numRows: int) -> str:
        """With a little hint I understand that it's easy to flip solution and
        process data by row instead of by column.
        Time: O(n)
        Space: O(n)
        """
        if numRows <= 1 or numRows > len(s):
            return s

        # it's possible to use string but it will result in higher time
        # complexity, due to string concatenation nature
        res = [list() for x in range(numRows)]
        row = 0

        for char in s:
            res[row].append(char)

            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1

            row += step

        # O(n/numRows) * NumRows = O(n)
        return "".join("".join(x) for x in res)


@pytest.mark.parametrize(
    "solution", [Solution, Solution2]
)
@pytest.mark.parametrize(
    "input_str,num,expected_output",
    (
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("AB", 1, "AB"),
    )
)
def test_combine(solution, input_str, num, expected_output):
    assert solution().convert(input_str, num) == expected_output
