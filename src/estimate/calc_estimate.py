from src.print.print_second_derivatives_estime import print_second_derivatives_estime


def frange(start, end=None, inc=None):
    "A range function, that does accept float increments..."

    if end is None:
        end = start + 0.0
        start = 0.0

    if inc is None:
        inc = 1.0

    L = []
    while 1:
        next = start + len(L) * inc
        if inc > 0 and next >= end:
            break
        elif inc < 0 and next <= end:
            break
        L.append(next)

    return L


def calc_estimate(coords: list[tuple[float, float]], equi: float) -> list[tuple[float, float]]:
    index = 0

    for i, v in enumerate(coords):
        if v[1] == equi:
            index = i
            break
    a = (coords[index + 1][1] - coords[index - 1][1]) / (coords[index + 1][0] - coords[index - 1][0])
    b = coords[index + 1][1] - a * coords[index + 1][0]
    estimates = [a * i + b for i in frange(coords[index - 1][0], coords[index + 1][0], 0.1)]
    print_second_derivatives_estime(estimates)
    return estimates
