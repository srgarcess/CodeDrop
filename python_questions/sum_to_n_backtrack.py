import timeit
def sum_to_n_backtrack(test_input, target):
    results = []
    test_input.sort()

    def backtrack(remaining_sum, combination, start_index):
        if remaining_sum == 0:
            results.append(list(combination))
            return

        if remaining_sum < 0:
            return

        for i in range(start_index, len(test_input)):
            num = test_input[i]
            combination.append(num)
            backtrack(remaining_sum - num, combination, i)
            combination.pop()

    backtrack(target, [], 0)

    return results


def sum_to_n(test_input, target):
    output = []
    if target < 0:
        return []
    for i in range(len(test_input)):
        if target == test_input[i]:
            output.append([test_input[i]])
        else:
            for j in sum_to_n(test_input[i:], target-test_input[i]):
                output.append([test_input[i]]+j)
    return output


if __name__ == "__main__":
    test_input = [1,2,3,4,5]
    target = 25

    backtrack_runtime = timeit.timeit(lambda: sum_to_n_backtrack(test_input, target), number=5_000)
    backtrack_total_combinations = len(sum_to_n_backtrack(test_input, target))
    print(f"Backtrack: Total runtime for finding a total of {backtrack_total_combinations} combinations summing to {target}: {backtrack_runtime:.2f} seconds")

    sum_to_n_runtime = timeit.timeit(lambda: sum_to_n(test_input, target), number=5_000)
    sum_to_n_total_combinations = len(sum_to_n(test_input, target))
    print(f"Sum to N: Total runtime for finding a total of {sum_to_n_total_combinations} combinations summing to {target}: {sum_to_n_runtime:.2f} seconds")
    print("=== Code Execution Complete ===")
