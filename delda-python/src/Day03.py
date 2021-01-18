from globalFunctions import readInputFile


def solvePart1():
    inp = readInputFile('../data/Day03Input')
    return sudden_arboreal_stop(inp, 3, 1)


def solvePart2():
    inp = readInputFile('../data/Day03Input')
    return sudden_arboreal_stop(inp, 1, 1) \
           * sudden_arboreal_stop(inp, 3, 1) \
           * sudden_arboreal_stop(inp, 5, 1) \
           * sudden_arboreal_stop(inp, 7, 1) \
           * sudden_arboreal_stop(inp, 1, 2)


def sudden_arboreal_stop(map: list, x_slope: int, y_slope: int) -> int:
    y_len = len(map)
    x_len = len(map[0])
    x = 0
    trees = 0
    for y in range(y_slope, y_len, y_slope):
        x = (x + x_slope) % x_len
        if map[y][x] == '#':
            trees += 1
    return trees


print(solvePart1())
print(solvePart2())
