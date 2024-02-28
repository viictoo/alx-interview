## 0x08-making_change

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

Prototype: def makeChange(coins, total)
Return: fewest number of coins needed to meet total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
You can assume you have an infinite number of each denomination of coin in the list
Your solution’s runtime will be evaluated in this task

```
def topDown(coins, amount):
    '''
    :type coins: list of int
    :type amount: int
    :rtype: int
    '''
    if amount < 1:
        return 0

    return coin_change(coins, amount, [0] * (amount + 1))


def coin_change(coins, remainder, cache):
    """
        Minimum coins to make change for a negative amount is -1.
        This is just a base case we arbitrarily define.
    if remainder < 0:
        return -1

    The minimum coins needed to make change for 0 is always 0
    coins no matter what coins we have.
    """
    if remainder == 0:
        return 0

    # We already have an answer cached. Return it.
    if cache[remainder] != 0:
        return cache[remainder]

    # No answer yet. Try each coin as the last coin in the change that
    # we make for the amount
    system_max = sys.maxsize
    minimum = system_max
    for coin in coins:
        change_result = coin_change(coins, remainder - coin, cache)
        '''
        If making change was possible (changeResult >= 0) and
        the change result beats our present minimum, add one to
        that smallest value
        We accept that coin as the last coin in our change making
        sequence up to this point since it minimizes the coins we
        need
        '''
        if (change_result >= 0 and change_result < minimum):
            minimum = 1 + change_result

    '''
    If no answer is found (minimum == max value) then the
    sub problem answer is just arbitrarily made to be -1, otherwise
    the sub problem's answer is "minimum"
    '''
    cache[remainder] = -1 if (minimum == system_max) else minimum

    return cache[remainder]


def makeChange(coins, amount):
    """
    :type coins: list of int
    :type amount: int
    :rtype: int
    """

    # This table will store the answer to our sub problems
    dp = [amount + 1] * (amount + 1)

    '''
    The answer to making change with minimum coins for 0
    will always be 0 coins no matter what the coins we are
    given are
    '''
    dp[0] = 0

    # Solve every subproblem from 1 to amount
    for i in range(1, amount + 1):
        # For each coin we are given
        for j in range(0, len(coins)):
            # If it is less than or equal to the sub problem amount
            if coins[j] <= i:
                # Try it. See if it gives us a more optimal solution
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)

    '''
    dp[amount] has our answer. If we do not have an answer then dp[amount]
    will be amount + 1 and hence dp[amount] > amount will be true. We then
    return -1.

    Otherwise, dp[amount] holds the answer
    '''

    return -1 if dp[amount] > amount else dp[amount]

    ```