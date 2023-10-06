#!/usr/bin/python3
"""Solving lock boxes problem"""


def update_keys(box, count, keys):
    """Looks inside a box and updates a list of keys that can open the boxes

    Args:
        box: A list of keys.
        count: The number of boxes we have.
    """
    for key in box:
        if key < count and key not in keys:
            keys.append(key)


def canUnlockAll(boxes):
    """
    Determines if it is possible to unlock all the boxes in a list of boxes
    by following their contained keys.
    :param boxes: list of lists (boxes) each box contain some keys
    :return:
        True if all boxes can be unlocked False otherwise
    """
    i = 0
    unlocked = [0]

    while i < len(unlocked):
        update_keys(boxes[unlocked[i]], len(boxes), unlocked)
        i += 1
        if len(unlocked) == len(boxes):
            return True

    return False
