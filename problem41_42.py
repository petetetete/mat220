# Constants
TURNAROUND_START = [3, 5, 2, 6, 1, 4]
REVERSALS_START = [3, 1, 6, 5, -2, 4]

GOAL = [1, 2, 3, 4, 5, 6]


# Helper function used to reverse a subsequence in a list (with scalar)
def reverse(arr, a, b, c=1):
    new = arr[:]
    new[a:b] = [c * x for x in new[a:b][::-1]]
    return new


# Recursive function that brute forces a path to pancake sort
def turnaround(arr, goal, max_depth, sign_reversal=False, h=[]):

    # If we have reached the goal
    if arr == goal:
        return h

    # If we have bottomed out
    if max_depth == 0:
        return None

    # Get all possible starts (depending on the search type)
    possible_starts = range(len(arr) + 1) if sign_reversal else [0]
    for a in possible_starts:

        # Iterate over all possible subsequences
        for b in range(a + 1, len(arr) + 1):

            # Determine scalar and move history element depending on search
            scalar = -1 if sign_reversal else 1
            move = (a + 1, b) if sign_reversal else b

            # Recursively call self with new progress
            out = turnaround(reverse(arr, a, b, scalar), goal, max_depth - 1,
                             sign_reversal, h + [move])

            # If we have found a valid answer, break out
            if out is not None:
                return out


# Get answers
l1 = turnaround(TURNAROUND_START, GOAL, 6)
l2 = turnaround(REVERSALS_START, GOAL, 5, True)

# Print results
print("Problem 41")
print("----------")
print("Starting list:", TURNAROUND_START)
print("k values to reverse:", l1, "\n")

print("Problem 42")
print("----------")
print("Starting list:", REVERSALS_START)
print("Sub-sequences to Reverse:", l2)
