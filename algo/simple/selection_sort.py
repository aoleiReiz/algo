def selectionSort(array):
    # Write your code here.
    for i in range(len(array)):
        min_val = array[i]
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < min_val:
                min_val = array[j]
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

