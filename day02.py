def get_invalid_ids_in_range_part1(range_string: str) -> list[int]:
    lower_string, upper_string = range_string.split("-")
    lower = int(lower_string)
    upper = int(upper_string)
    if len(lower_string) % 2 == 0:
        min_repeated_number = int(lower_string[:len(lower_string) // 2])
    else:
        min_repeated_number = int("1" + "0" * (len(lower_string) // 2))
    if len(upper_string) % 2 == 0:
        max_repeated_number = int(upper_string[:len(upper_string) // 2])
    else:
        max_repeated_number = int("9" * (len(upper_string) // 2))

    invalid_ids = []
    for repeated_number in range(min_repeated_number, max_repeated_number + 1):
        repeated_number_id = int(str(repeated_number) * 2)
        if lower <= repeated_number_id <= upper:
            invalid_ids.append(repeated_number_id)

    return invalid_ids


def get_invalid_ids_in_range(range_string: str, repeat_twice: bool) -> list[int]:
    lower_string, upper_string = range_string.split("-")
    lower = int(lower_string)
    upper = int(upper_string)

    invalid_ids = []

    max_repetition = 2 if repeat_twice else len(upper_string)
    for repetition in range(2, max_repetition + 1):
        if len(lower_string) % repetition == 0:
            min_repeated_number = int(lower_string[:len(lower_string) // repetition])
        else:
            min_repeated_number = int("1" + "0" * (len(lower_string) // repetition))
        if len(upper_string) % repetition == 0:
            max_repeated_number = int(upper_string[:len(upper_string) // repetition])
        else:
            max_repeated_number = int("9" * (len(upper_string) // repetition))

        for repeated_number in range(min_repeated_number, max_repeated_number + 1):
            repeated_number_id = int(str(repeated_number) * repetition)
            if lower <= repeated_number_id <= upper and repeated_number_id not in invalid_ids:
                invalid_ids.append(repeated_number_id)

    return invalid_ids


def get_invalid_ids(ranges: list[str], repeat_twice: bool = True) -> int:
    invalid_ids = []
    for range_string in ranges:
        invalid_ids.extend(get_invalid_ids_in_range(range_string, repeat_twice))
    return sum(invalid_ids)


if __name__ == "__main__":
    with open("day02_input.txt") as f:
        input_string = f.read()
    ranges = input_string.split(",")
    # Part 1
    print(get_invalid_ids(ranges))
    # Part 2
    print(get_invalid_ids(ranges, repeat_twice=False))
