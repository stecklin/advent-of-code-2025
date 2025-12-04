def get_joltage_per_bank_part1(bank: str) -> int:
    digits = [int(char) for char in bank]
    max_first_digit = max(digits[:-1])
    max_first_digit_index = digits.index(max_first_digit)
    max_second_digit = max(digits[max_first_digit_index + 1:])
    joltage = int(str(max_first_digit) + str(max_second_digit))
    return joltage


def get_joltage_per_bank(bank: str, num_batteries: int) -> int:
    digits = [int(char) for char in bank]
    joltage = ""
    for digit_pos in range(num_batteries):
        max_digit = max(digits[:len(digits) - num_batteries + digit_pos + 1])
        last_digit_index = digits.index(max_digit)
        digits = digits[last_digit_index + 1:]
        joltage += str(max_digit)
    joltage = int(joltage)
    return joltage


def get_joltage(banks: list[str], num_batteries: int = 2) -> int:
    joltage_sum = 0
    for bank in banks:
        joltage_sum += get_joltage_per_bank(bank, num_batteries)
    return joltage_sum


if __name__ == "__main__":
    with open("day03_input.txt") as f:
        banks = f.read().splitlines()
    # Part 1
    print(get_joltage(banks))
    # Part 2
    print(get_joltage(banks, num_batteries=12))
