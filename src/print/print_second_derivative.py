def print_second_derivatives(values: list[tuple[float, float]]) -> int:
    print("Second derivative:")
    for value in values:
        print(f"{value[0]:.1f} ml -> {value[1]:.2f}")
    return 0
