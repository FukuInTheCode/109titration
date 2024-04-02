from src.calc_derivative import calc_derivative


def calc_first_derivative(coords: list[tuple(float, float)]) -> list[tuple(float, float)]:
    first_der = calc_derivative(coords)
    print_derivatives(first_der)
    return first_der
