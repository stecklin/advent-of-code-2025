def check_available_ingredient_ids_idea1(id_ranges: list[str], ingredient_ids: list[str]) -> int:
    fresh_ingredient_ids = set()
    for id_range in id_ranges:
        low, high = id_range.split("-")
        fresh_ingredient_ids.update(range(int(low), int(high) + 1))
    num_fresh_ingredient_ids = 0
    for ingredient_id in ingredient_ids:
        if int(ingredient_id) in fresh_ingredient_ids:
            num_fresh_ingredient_ids += 1
    return num_fresh_ingredient_ids


def check_available_ingredient_ids(id_ranges: list[str], ingredient_ids: list[str]) -> int:
    num_fresh_ingredient_ids = 0
    for ingredient_id in ingredient_ids:
        for id_range in id_ranges:
            low, high = id_range.split("-")
            if int(low) <= int(ingredient_id) <= int(high):
                num_fresh_ingredient_ids += 1
                break
    return num_fresh_ingredient_ids


def get_low_high(id_range: str) -> tuple[int, int]:
    low, high = id_range.split("-")
    return int(low), int(high)


def count_fresh_ingredient_ids(id_ranges: list[str]) -> int:
    lows_highs = [get_low_high(id_range) for id_range in id_ranges]
    num_fresh_ingredient_ids = 0
    while lows_highs:
        low, high = lows_highs.pop()
        stop = False
        while not stop:
            stop = True
            for i in range(len(lows_highs) - 1, -1, -1):
                low_i, high_i = lows_highs[i]
                if low_i > high or high_i < low:
                    continue
                if low_i < low:
                    low = low_i
                if high_i > high:
                    high = high_i
                stop = False
                lows_highs.pop(i)
        num_fresh_ingredient_ids += high - low + 1
    return num_fresh_ingredient_ids


if __name__ == "__main__":
    with open("day05_input.txt") as f:
        input_string = f.read()
    id_ranges, ingredient_ids = input_string.split("\n\n")
    id_ranges = id_ranges.split("\n")
    ingredient_ids = ingredient_ids.split("\n")
    # Part 1
    print(check_available_ingredient_ids(id_ranges, ingredient_ids))
    # Part 2
    print(count_fresh_ingredient_ids(id_ranges))
