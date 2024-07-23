"""
Question:
-------------------------------------------------------------------
Have the function bracket_combinations(num) read
num which will be an integer greater than or equal to
zero, and return the number of valid combinations that
can be formed with num pairs of parentheses. For
example, if the input is 3, then the possible combinations
of 3 pairs of parenthesis, namely: ()()(), are ()()(), ()(()),
(())(), ((())), and (()()). There are 5 total combinations
when the input is 3, so your program should return 5.
-------------------------------------------------------------------
This problem is an example of both
- dyck paths problem (https://en.wikipedia.org/wiki/Dyck_Paths)
- balanced parenthesis problem (https://en.wikipedia.org/wiki/Balanced_parenthesis)
"""
import math


def bracket_combinations(num: int) -> int:
    if num == 0:
        return 1
    return math.comb(2*num, num)//(num + 1)


def bracket_combinations2(num: int) -> int:
    """
    This is without using comb method in the math library
    :param num:
    :return:
    """
    def fact(n):
        if n == 0 or n == 1:
            return 1
        return n * fact(n - 1)

    return fact(2*num) // (fact(num) * fact(num) * (num + 1))


if __name__ == '__main__':
    for i in range(11):
        print(bracket_combinations(i), end=" | ")
    print()

    for i in range(11):
        print(bracket_combinations2(i), end=" | ")
    print()
