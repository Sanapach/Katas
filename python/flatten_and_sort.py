def flatten_and_sort(array):
    result = [value for sublist in array for value in sublist]
    print(sorted(result))


flatten_and_sort([[3, 2, 1], [4, 6, 5], [], [9, 7, 8]])