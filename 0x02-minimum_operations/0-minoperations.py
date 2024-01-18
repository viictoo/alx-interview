#!/usr/bin/python3
"""
Main file for testing
"""


def minOperations(n: int) -> int:
    """Returns the minimum operations required to archieve n characters."""
    # if n <= 1:
    #     return 0
    # else:
    #     for i in range(2, n + 1):
    #         if n % i == 0:
    #             return minOperations(n // i) + i
    #     return n

    result = 0
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                result += i
                n = n // i
                break
    return result

    # x, count, paste, copyAll = 1, 1, 1, 1
    # while (x < n):

    #     if (n == 1):
    #         return count

    #     copyAll = x + x
    #     paste = x
    #     if (n % copyAll == 0):
    #         return ((n // copyAll) + count)
    #     elif (n % (copyAll + paste) == 0):
    #         return (n // (copyAll + paste)) + count
    #     paste = x
    #     count += 1
    #     x += 1

    # if (n % paste == 0 and n > 1):
    #     x += paste
    #     print("x", x)
    #     print("paste",paste)
    #     print('paste', paste)
    #     print('count', count)

    #     return (n // paste) + count
    #     # count += 2
    # else:
    #     x = copy
    #     print('copy', x)
    #     count += 1

    # print(x)
    # return count if x == n else False


if __name__ == '__main__':

    n = 1
    print("Min # of operations to reach {} char: {}".format(
        n, minOperations(n)))
    n = 3
    print("Min # of operations to reach {} char: {}".format(
        n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(
        n, minOperations(n)))
    n = 12
    print("Min # of operations to reach {} char: {}".format(
        n, minOperations(n)))
    n = 12
    print("Min # of operations to reach {} char: {}".format(
        n, minOperations(n)))
