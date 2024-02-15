#!/usr/bin/python3

"""Prime Game"""


def sqrt(n):
    """square root function"""
    if n < 0:
        raise (ValueError("Cannot square a negative number"))
    return n ** 0.5


def is_prime(n):
    """Determine if a number is prime"""
    if n <= 1:
        return False
    if n in (2, 3):
        return True

    if n % 2 == 0:
        return False

    for i in range(5, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def remove_prime_multiples(nums: list):
    """Selects the first prime in the list and removes it and it's multiples"""
    new_nums = nums[:]
    no_prime = True
    chosen = 0
    for num in nums:
        if chosen == 0:
            if is_prime(num):
                no_prime = False
                chosen = num
                new_nums.remove(num)

        elif num % chosen == 0:
            new_nums.remove(num)

    return None if no_prime else new_nums


def round_winner(n):
    """Determines round winner"""
    maria_turn = True
    nums = list(range(1, n + 1))
    nums = remove_prime_multiples(nums)

    while nums is not None:
        maria_turn = not maria_turn
        nums = remove_prime_multiples(nums)

    return "Ben" if maria_turn else "Maria"


def isWinner(x, nums):
    """
    Determine the winner Maria or Ben in prime game
    Maria always start
    :param x: number of rounds
    :param nums: array of numbers
    :return: The winner
    """
    winnings = {"Maria": 0, "Ben": 0}

    for round in range(x):
        if round >= len(nums):
            break
        winner = round_winner(nums[round])
        winnings[winner] += 1

    if winnings["Maria"] > winnings["Ben"]:
        return "Maria"
    elif winnings["Maria"] < winnings["Ben"]:
        return "Ben"
    else:
        return None
