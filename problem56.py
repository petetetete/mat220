from itertools import permutations

# Create list of combination options
choices = ["".join(p) for p in permutations("abcd")]
combinations = [
    [c for c in choices if c[3] == "a"],
    choices,
    choices,
    choices,
    [c for c in choices if c[3] == "d"],
    [c for c in choices if c[2] == "b"],
    [c for c in choices if c[1] == "d"],
    [c for c in choices if c[2] == "c"],
    [c for c in choices if c[3] == "b"],
    [c for c in choices if c[1:3] == "ac"],
    [c for c in choices if c[0:2] == "db"],
    choices,
    [c for c in choices if c[2:4] == "ba"],
    [c for c in choices if c[0] == "a"],
    [c for c in choices if c[1:3] == "cb"],
    [c for c in choices if c[0] == "b"],
    [c for c in choices if c[2] == "c"],
    [c for c in choices if c[1] == "b"],
    [c for c in choices if c[3] == "d"],
    [c for c in choices if c[1:3] == "bc"],
    [c for c in choices if c[0] == "a"],
    [c for c in choices if c[2] == "c"],
    [c for c in choices if c[0] == "b" and c[3] == "a"],
    [c for c in choices if c[1] == "b"],
]


# Helper function used to determine row validity
def isValidRow(board, row):
    return (row not in board and
            all(c != row[i] for i, c in enumerate(board[-1])))


# Recursive function that takes in a combinations array
def findBoard(combs, board=[]):

    # Base case on empty combinations array
    if len(combs) == 0:
        return board

    # Get subset of combination strings that are valid
    valid_strings = [s for s in combs[0]
                     if len(board) == 0 or isValidRow(board, s)]

    # Recursively call self for each string
    for string in valid_strings:
        out = findBoard(combs[1:], board + [string])

        # If we found a winning board
        if out is not None:
            return out


# Execute and print
result = findBoard(combinations)
print("\n".join([" | ".join(r) for i, r in enumerate(result)]))
