def print_derivatives(values: list[tuple[float, float]]) -> int:
    print("Derivative:")
    for value in values:
        print(f"{value[0]:.1f} ml -> {value[1]:.2f}")
    return 0
