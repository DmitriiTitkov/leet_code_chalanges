"""

"""


class Solution:
    def calculate(self, s: str) -> int:

        def sub_calc(start, finish) -> int:
            cur_eval = 0
            operation = "+"
            i = start
            sub_finish = finish

            while i <= finish:
                cur_num = 0

                if s[i] == " ":
                    i += 1
                    continue

                if s[i] in ("+", "-"):
                    operation = s[i]
                    i += 1
                    continue
                elif s[i] == "(":
                    cur_num, sub_finish = sub_calc(i + 1, finish)
                    i = sub_finish
                elif s[i] == ")":
                    return cur_eval, i
                else:
                    num_start = num_end = i

                    while i < len(s) and s[i].isdigit():
                        num_end = i
                        i += 1
                    i -= 1
                    cur_num = int(s[num_start:num_end + 1])

                if operation == "+":
                    cur_eval += cur_num
                else:
                    cur_eval -= cur_num

                i += 1

            return cur_eval, sub_finish

        return sub_calc(0, len(s) - 1)[0]

