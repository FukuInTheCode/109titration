from src.calc_derivative import calc_derivative


def calc_second_derivative(coords: list[tuple(float, float)]) -> list[tuple(float, float)]:
    second_derivative = calc_derivative(coords)
    print_second_derivatives(second_derivative)
    return second_derivative
