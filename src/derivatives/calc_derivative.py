def calc_derivative(coords: list[tuple[float, float]]) -> list[tuple[float, float]]:
    der = []

    for i in range(1, len(coords) - 1, 1):
        der.append(
            (
                coords[i][0],
                (
                    (coords[i + 1][1] - coords[i][1]) / (coords[i + 1][0] - coords[i][0])
                    + (coords[i][1] - coords[i - 1][1]) / (coords[i][0] - coords[i - 1][0])
                )
                / (coords[i + 1][0] - coords[i - 1][0]),
            )
        )
    return der
