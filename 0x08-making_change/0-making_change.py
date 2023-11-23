#!/usr/bin/python3

"""Solving change coins problem"""


def makeChange(coins, total):
    """Calculates the minimum number of coins needed to make the total amount"""
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for a in range(1, total + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], dp[a - c] + 1)

    return dp[total] if dp[total] != total + 1 else -1
