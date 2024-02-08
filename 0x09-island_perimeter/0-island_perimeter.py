#!/usr/bin/python3

"""Island Perimeter Solution"""


def island_perimeter(grid) -> int:
    """
    Returns the perimeter of an island
    args:
    gird (list): the grid
    """

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
