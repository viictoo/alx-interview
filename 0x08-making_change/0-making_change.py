#!/usr/bin/python3
"""" tech interview question """


def makeChangeRecursive(coins, total):
    """why is this faster?"""
    result = []
    current = -1
    coins = sorted(coins, reverse=True)

    def dfs(comb=[], sum=float('-inf'), start=0, current=[]):
        """backtracking to eliminate unused options"""
        if sum > total:
            return
        elif sum == total:
            current = min(len(current, len(comb)))
            return
        for i in range(start, len(coins)):

            if sum+coins[i] > target:
                continue
            comb.append(coins[i])
            dfs(comb, i, sum+coins[i])
            comb.pop()

    dfs(coins, total)
    return result


def makeChange(deno, V):
    """generatare all possible coins to make total"""
    if V <= 0:
        return 0
    n = len(deno)
    deno = sorted(deno)

    ans = []
    i = n - 1
    while (i >= 0):

        # Find denominations
        while (V >= deno[i]):
            V -= deno[i]
            ans.append(deno[i])

        i -= 1
    if V != 0:
        return -1
    if ans == []:
        return -1
    return len(ans)


# Driver Code
if __name__ == '__main__':

    print(makeChange([1, 2, 25], 37))

    print(makeChange([1256, 54, 48, 16, 102], 1453))
