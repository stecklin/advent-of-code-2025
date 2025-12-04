def get_dial_position(old_position: int, rotation: str, any_click_at_0: bool) -> tuple[int, int]:
    if rotation[0] == "L":
        direction = -1
    elif rotation[0] == "R":
        direction = 1
    else:
        raise ValueError("Invalid rotation")
    rotation = int(rotation[1:])

    new_position_unnormalized = old_position + direction * rotation
    new_position = new_position_unnormalized % 100

    if any_click_at_0 and new_position_unnormalized >= 100:
        clicks_at_0 = new_position_unnormalized // 100
    elif any_click_at_0 and new_position_unnormalized <= 0:
        clicks_at_0 = -1 * ((new_position_unnormalized - 1) // 100)
        if old_position == 0:
            clicks_at_0 -= 1
    elif not any_click_at_0 and new_position == 0:
        clicks_at_0 = 1
    else:
        clicks_at_0 = 0

    return new_position, clicks_at_0


def get_password(rotations: list[str], any_click_at_0: bool = False) -> int:
    dial_position = 50
    password = 0
    for rotation in rotations:
        dial_position, clicks_at_0 = get_dial_position(dial_position, rotation, any_click_at_0)
        password += clicks_at_0
    return password


if __name__ == "__main__":
    with open("day01_input.txt") as f:
        rotations = f.read().splitlines()
    # Part 1
    print(get_password(rotations))
    # Part 2
    print(get_password(rotations, any_click_at_0=True))
