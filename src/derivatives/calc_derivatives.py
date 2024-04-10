from src.derivatives.calc_first_derivative import calc_first_derivative
from src.equivalence.find_equivalence import find_equivalence
from src.print.print_equivalence import print_equivalence
from src.derivatives.calc_second_derivative import calc_second_derivative
from src.estimate.calc_estimate import calc_estimate


def calc_derivatives(coords: list[tuple[float, float]]) -> int:
    first = calc_first_derivative(coords)
    equi = find_equivalence(first)
    print_equivalence(equi[0])
    print()
    second = calc_second_derivative(first)
    estimates = calc_estimate(second, equi[0])
    mini = estimates[0]
    for x, y in estimates[1:]:
        if abs(mini[1]) > abs(y):
            mini = (x, y)
    print_equivalence(mini[0])
    return 0
