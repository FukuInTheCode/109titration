def find_equivalence(coords: list[tuple(float, float)]) -> list[tuple(float, float)]:
    equi = coords[0]

    for i in range(1, len(coords)):
        if equi[1] < coords[i][1]:
            equi = coords[i]
    return equi[0]
