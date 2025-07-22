"""
Write a Python function to find the maximum subarray sum in a given array of integers.
The function should return a list containing the maximum sum, the start index, and the end index of the subarray.

Constraints
The input variable must be a list of integers.
The function must return a list with three elements: the maximum sum (an integer), the start index (an integer), and the end index (an integer).
The function should use an iterative approach and cannot use eval or lambda functions.
"""
def max_subarray_sum(arr):
    if not arr:
        return []

    max_sum = current_sum = arr[0]
    start = end = s = 0

    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            s = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = s
            end = i

    return [max_sum, start, end]

# Test cases for the max_subarray_sum function
test1 =[-2, 1, -3, 4, -1, 2, 1, -5, 4]
test2 = [1, 2, 3, 4, 5]
test3 = [-1, -2, -3, -4, -5]
test4 = [5, -2, 3, -1, 2, -1, 2, -3, 4]
test5 = [0, -3, 1, -2, 3, 4, -1, 2, 1]
test6 = [-4,2,-5,1,6,-3,2,-1]
test7 = [i for i in test3[::-1]]

all_tests = [test1, test2, test3, test4, test5, test6, test7]

for i in range(len(all_tests)):
    print(f"Test {i+1}:", max_subarray_sum(all_tests[i]))

print("== Code Execution Complete ==")