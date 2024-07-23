"""
Question:
Have the function bracket_combinations(num) read
num which will be an integer greater than or equal to
zero, and return the number of valid combinations that
can be formed with num pairs of parentheses. For
example, if the input is 3, then the possible combinations
of 3 pairs of parenthesis, namely: ()()(), are ()()(), ()(()),
(())(), ((())), and (()()). There are 5 total combinations
when the input is 3, so your program should return 5.
"""
import math


def bracket_combinations(num: int) -> int:
    if num == 0:
        return 1
    return math.comb(2*num, num)//(num + 1)
    # keep this function call here


if __name__ == '__main__':
    print(bracket_combinations(int(input())))
