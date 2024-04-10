from src.derivatives.calc_derivative import calc_derivative
from src.print.print_second_derivative import print_second_derivatives


def calc_second_derivative(coords: list[tuple[float, float]]) -> list[tuple[float, float]]:
    second_derivative = calc_derivative(coords)
    print_second_derivatives(second_derivative)
    print()
    return second_derivative
