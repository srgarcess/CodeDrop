# xy_interval.py
import math
import timeit
from itertools import product
"""
Let f(x, y) = 5^x * 3^y.
Given an interval [L, R] and a limit N, write a function,
`get_possible_values(L, R, N)` that returns all positive pairs (x,y) such that
L <= f(x, y) <= R and 0 <= x, y < N.
"""

# Brute force solution to find all pairs (i, j) such that L <= 5^i * 3^j <= R
def get_possible_values_bf(L, R, N):
    return [(x,y) for x in range(N) for y in range(N) if L <= (5**x) * (3**y) <= R]

# Early Stopping Optimized solution to find all pairs (i, j) such that L <= 5^i * 3^j <= R
def get_possible_values_es(L, R, N):
    results = []
    if R == 0:
        return [[0, 0]] if L == 0 else []
    for x in range(N):
        val_5_x = 5**x
        # Early exit for the outer loop: if 5^x alone already exceeds R,
        # then any subsequent 5^x * 3^y (where y >= 0) will also exceed R.
        if val_5_x > R:
            break
        for y in range(N):
            current_value = val_5_x * (3**y)
            # Early exit for the inner loop: if current_value exceeds R,
            # then any subsequent 5^x * 3^(y+1) will also exceed R (for the same x).
            if current_value > R:
                break
            if L <= current_value <= R:
                results.append([x, y])
    return results

# Log solution to find all pairs (i, j) such that L <= 5^i * 3^j <= R
def get_possible_values_log(L, R, N):
    if R == 0:
        return [[0, 0]] if L == 0 else []

    max_x = int(math.log(R, 5)) + 1
    max_y = int(math.log(R, 3)) + 1

    results = []
    for x, y in product(range(min(N, max_x)), range(min(N, max_y))):
        current_value = (5**x) * (3**y)
        if L <= current_value <= R:
            results.append([x, y])
    return results

if __name__ == "__main__":
    # Example usage
    L = 0
    R = 100
    N = 100
    iters = 10**3
    result_bf_runtime = timeit.timeit(lambda: get_possible_values_bf(L, R, N), number=iters)
    result_es_runtime = timeit.timeit(lambda: get_possible_values_es(L, R, N), number=iters)
    result_log_runtime = timeit.timeit(lambda: get_possible_values_log(L, R, N), number=iters)

    print(f"Brute Force Runtime: {result_bf_runtime:.2f} seconds")
    print(f"Early Stopping Runtime: {result_es_runtime:.2f} seconds")
    print(f"Log Runtime: {result_log_runtime:.2f} seconds")
    print("=== Code Execution Complete ===")
