#!/usr/bin/python3
"""Solving lock boxes problem"""


def look_inside(box, count):
    """Looks inside a box and returns a list of keys that are less than the
    specified count.

    Args:
        box: A set of keys.
        count: The number of boxes we have.

    Returns:
        A list of keys that are less than the specified count.
    """
    return {key for key in box if key < count}


def canUnlockAll(boxes):
    """
    Determines if it is possible to unlock all the boxes in a list of boxes
    by following their contained keys.
    :param boxes: list of lists (boxes) each box contain some keys
    :return:
        True if all boxes can be unlocked False otherwise
    """

    if type(boxes) is not list or len(boxes) == 0:
        return False

    i = 0
    unlocked = {0}

    while i < len(unlocked):
        if type(boxes[i]) is not list:
            return False
        keys = look_inside(boxes[i], len(boxes))
        unlocked.update(keys)
        i += 1
        if len(unlocked) == len(boxes):
            return True

    return False
