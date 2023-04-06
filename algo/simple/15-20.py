def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def findThreeLargestNumbers(array):
    first_large = float("-inf")
    second_large = float("-inf")
    third_large = float("-inf")

    for num in array:
        if num > first_large:
            first_large, second_large, third_large = num, first_large, second_large
        elif num > second_large:
            second_large, third_large = num, second_large
        elif num > third_large:
            third_large = num

    return [third_large, second_large, first_large]


def bubbleSort(array):
    n = len(array)
    for i in range(n):
        flag = False
        for j in reversed(range(n - 1)):
            if array[j + 1] < array[j]:
                array[j + 1], array[j] = array[j], array[j + 1]
                flag = True
        if not flag:
            break
    return array


def insertionSort(array):
    for i, num in enumerate(array):
        j = i
        while j > 0 and array[j - 1] > num:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
        array[j] = num
    return array


def selectionSort(array):
    for i, num in enumerate(array):
        min_idx = i
        min_ele = num
        for j in range(i + 1, len(array)):
            if array[j] < min_ele:
                min_ele = array[j]
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array
