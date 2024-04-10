def calc_derivative(coords: list[tuple[float, float]]) -> list[tuple[float, float]]:
    der = []

    for i in range(1, len(coords) - 1):
        x_i, y_i = coords[i]
        x_prev, y_prev = coords[i - 1]
        x_next, y_next = coords[i + 1]

        h1 = x_i - x_prev
        h2 = x_next - x_i

        # Weighted average of forward and backward rates
        slope = ((y_next - y_i) / h2 + (y_i - y_prev) / h1) / (h1 + h2)

        der.append((x_i, slope))

    return der
