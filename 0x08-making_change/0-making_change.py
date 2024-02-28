#!/usr/bin/python3
"""" tech interview question """


def makeChange(deno, total):
    """generate all possible coins to make total"""
    if total <= 0:
        return 0

    n = len(deno)
    deno = sorted(deno)
    ans = []
    i = n - 1
    while (i >= 0):
        while (total >= deno[i]):
            total -= deno[i]
            ans.append(deno[i])
        i -= 1
    if total != 0:
        return -1
    return len(ans) if ans else -1


if __name__ == '__main__':

    print(makeChange([1, 2, 25], 37))

    print(makeChange([1256, 54, 48, 16, 102], 1453))
