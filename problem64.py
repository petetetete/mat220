# Python imports
from itertools import permutations
from time import time


def row_is_valid(row, prev_rows):
    """Helper method used to determine if a new row is valid"""

    # If there is any column duplication
    for i in range(len(row)):
        if any(x[i] == row[i] for x in prev_rows):
            return False

    # If there is any diagonal duplication
    row_i = len(prev_rows)
    if any((r[i] == row[row_i] or r[-(1 + i)] == row[-(1 + row_i)]
            for i, r in enumerate(prev_rows))):
        return False

    # There were no problems, row must be valid!
    return True


def find_boards_recurse(choices, rows, size=1):
    """Recursively create valid boards"""

    # Base case to return complete board configurations
    if size == 1:
        return [rows]

    # Iterate over all valid row choices
    outs = []
    for choice in [c for c in choices if row_is_valid(c, rows)]:

        # Find and save the recursive result if valid
        outs += find_boards_recurse(choices, rows + [choice], size - 1)

    # Return all solutions
    return outs


def find_boards(letters, print_n=3):
    """Find all valid configurations of boards given letter"""

    # Variable initialization
    choices = ["".join(p) for p in permutations(letters)]
    solutions = []
    start = time()

    # Iterate over starting positions
    for i, choice in enumerate(choices):
        solutions += find_boards_recurse(choices, [choice], len(letters))
        print("Solutions for start position", i + 1, "found", end="\r")

    # Calculate final stats
    total_time = round(time() - start, 2)
    num_solutions = len(solutions)
    print_n = min(num_solutions, print_n)

    # Print final stats
    print("\n\n### Final Stats ###\n")
    print("Number of solutions:", num_solutions)
    print("Total calculation time:", total_time, "seconds")

    # Print the first n solutions
    if print_n > 0:
        print("\n### First", str(print_n), "Solutions ###")
        for n in range(print_n):
            print("\nSolution", n + 1)
            print("-" * (9 + len(str(n + 1))))
            print("\n".join([" ".join(r) for r in solutions[n]]))


# Start the finding
find_boards("abcde")
