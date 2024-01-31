#!/usr/bin/python3

"""Solving change coins problem"""
from typing import List

def makeChange(coins: List[int], total: int) -> int:
    """Calculates the minimum amount of coins needed to make the total"""

    if total <= 0:
        return 0

    db = [(total + 1) for _ in range(total + 1)]
    db[0] = 0

    for a in range(1, total + 1):
        for c in coins:
            if a - c >= 0:
                db[a] = min(db[a], db[a - c] + 1)


    return db[total] if db[total] != (total + 1) else -1
