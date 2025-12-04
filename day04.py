import numpy as np
from scipy.signal import convolve2d


def get_accessible_rolls(diagram: np.ndarray) -> int:
    rolls = diagram == "@"
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    surrounding_rolls = convolve2d(rolls, kernel, mode="same")
    accessible_rolls = (rolls == 1) & (surrounding_rolls < 4)
    num_accessible_rolls = accessible_rolls.sum()
    return num_accessible_rolls


def get_removable_rolls(diagram: np.ndarray) -> int:
    rolls = diagram == "@"
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    num_removable_rolls = 0
    while True:
        surrounding_rolls = convolve2d(rolls, kernel, mode="same")
        accessible_rolls = (rolls == 1) & (surrounding_rolls < 4)
        num_accessible_rolls = accessible_rolls.sum()
        if num_accessible_rolls > 0:
            num_removable_rolls += num_accessible_rolls
            rolls = rolls & np.invert(accessible_rolls)
        else:
            break
    return num_removable_rolls


if __name__ == "__main__":
    diagram = np.genfromtxt("day04_input.txt", dtype=str, ndmin=2, delimiter=1)
    # Part 1
    print(get_accessible_rolls(diagram))
    # Part 2
    print(get_removable_rolls(diagram))
