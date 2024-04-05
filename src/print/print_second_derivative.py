def print_derivatives(values: list[list[float, float]]) -> int:
    print("Second derivative:")
    for value in values:
        print(f"{value[0]:.1f} ml -> {value[1]:.2f}")
    return 0
