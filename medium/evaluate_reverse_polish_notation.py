"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, and /. Each operand may be an integer or another
expression. Note that division between two integers should truncate toward zero.
It is guaranteed that the given RPN expression is always valid. That means the
expression would always evaluate to a result, and there will not be any
division by zero operation.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22


Constraints:
1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the
range [-200, 200].
"""
import math
import operator
from typing import List

import pytest


class Solution:
    def operate(self, first: int, second: int, op: str) -> int:
        operation_map = {
            "*": operator.mul,
            "/": lambda a, b: math.trunc(a / b),
            "+": operator.add,
            "-": operator.sub,
        }
        return operation_map[op](first, second)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"*", "/", "+", "-"}

        for token in tokens:
            if token in operators:
                second = stack.pop()
                first = stack.pop()

                res = self.operate(first, second, token)
                stack.append(res)

            else:
                stack.append(int(token))

        return stack.pop()


@pytest.mark.parametrize(
    "tokens,expected_output", (
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22)
    )
)
def test_eval_rpn(tokens, expected_output):
    assert Solution().evalRPN(tokens) == expected_output
