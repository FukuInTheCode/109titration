from src.derivatives.calc_derivative import calc_derivative
from src.print.print_derivatives import print_derivatives


def calc_first_derivative(coords: list[tuple[float, float]]) -> list[tuple[float, float]]:
    first_der = calc_derivative(coords)
    print_derivatives(first_der)
    return first_der
