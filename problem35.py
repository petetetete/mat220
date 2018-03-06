# Constants
START_POINT = (1, 0)
MAX_DEPTH = 18
TABLE_Y_RANGE = (8, 16)  # Inclusive table range
TABLE_X_RANGE = (1, 16)  # Inclusive table range


# Recursively get possible move positions
def getMoves(point, depth=0):
    if depth == MAX_DEPTH:
        return [point]

    return ([point] +
            getMoves((point[0], point[0] + point[1]), depth + 1) +
            getMoves((point[0] + point[1], point[1]), depth + 1))


# Generate possible points
data = getMoves(START_POINT)

# Print grid of reachable points
for x in range(TABLE_X_RANGE[0], TABLE_X_RANGE[1] + 1):
    for y in range(TABLE_Y_RANGE[0], TABLE_Y_RANGE[1] + 1):
        print("{0: >9} {1: <7}".format("(" + str(x) + ", " + str(y) + "):",
                                       str((x, y) in data)), end="")
    print()
