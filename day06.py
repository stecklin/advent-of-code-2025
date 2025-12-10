import operator

import numpy as np


def get_grand_total_part1(worksheet: np.ndarray) -> int:
    grand_total = 0
    for col in range(worksheet.shape[1]):
        if worksheet[-1, col] == "+":
            grand_total += worksheet[:-1, col].astype(int).sum()
        else:
            grand_total += worksheet[:-1, col].astype(int).prod()
    return grand_total


def get_grand_total_part2(worksheet: np.ndarray) -> int:
    grand_total = 0
    for col in range(worksheet.shape[1]):
        if worksheet[-1, col] == "+":
            op = operator.add
            problem_total = 0
        elif worksheet[-1, col] == "*":
            op = operator.mul
            problem_total = 1
        elif (worksheet[:, col] == " ").all():
            grand_total += problem_total
            continue
        number = int("".join(worksheet[:-1, col].tolist()))
        problem_total = op(problem_total, number)
    grand_total += problem_total
    return grand_total


if __name__ == "__main__":
    # Part 1
    worksheet = np.genfromtxt("day06_input.txt", dtype=str)
    print(get_grand_total_part1(worksheet))
    # Part 2
    worksheet = np.genfromtxt("day06_input.txt", dtype=str, delimiter=1)
    print(get_grand_total_part2(worksheet))

