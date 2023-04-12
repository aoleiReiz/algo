def threeNumberSum(array, targetSum):
    def two_sum(left, right, t):
        two_sum_result = []
        while left < right:
            s = array[left] + array[right]
            if s == t:
                two_sum_result.append([array[left], array[right]])
                left += 1
                right -= 1
            elif s > t:
                right -= 1
            else:
                left += 1
        return two_sum_result

    if len(array) < 3:
        return []
    array = sorted(array)
    ans = []
    for idx in range(len(array) - 2):
        for r in two_sum(idx + 1, len(array) - 1, targetSum - array[idx]):
            ans.append([array[idx], *r])
    return ans


def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne = sorted(arrayOne)
    arrayTwo = sorted(arrayTwo)
    closest_diff = float("inf")
    closest_pairs = []
    idx1 = 0
    idx2 = 0
    while idx1 < len(arrayOne) and idx2 < len(arrayTwo):
        num1 = arrayOne[idx1]
        num2 = arrayTwo[idx2]
        diff = abs(num1 - num2)
        if diff < closest_diff:
            closest_diff = diff
            closest_pairs = [num1, num2]
        if num1 > num2:
            idx2 += 1
        elif num1 < num2:
            idx1 += 1
        else:
            return [num1, num2]

    return closest_pairs


def moveElementToEnd(array, toMove):
    # Write your code here.
    left = 0
    right = len(array) - 1

    while left < right:
        while array[left] != toMove and left < right:
            left += 1
        while right > left and array[right] == toMove:
            right -= 1
        if left == right:
            break
        else:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    return array


def isMonotonic(array):
    n = len(array)
    if n <= 1:
        return True
    non_inc_flag  = True
    non_dec_flag = True
    for i in range(1, n):
        if array[i] > array[i-1]:
            non_inc_flag = False
        elif array[i] < array[i - 1]:
            non_dec_flag = False
    return non_inc_flag or non_dec_flag


def spiralTraverse(array):
    # Write your code here.
    if len(array) == 0:
        return []
    ans = []
    row_start = 0
    row_end = len(array) - 1
    col_start = 0
    col_end = len(array[0]) - 1
    while row_start <= row_end and col_start <= col_end:
        for c in range(col_start, col_end + 1):
            ans.append(array[row_start][c])
        row_start += 1
        for r in range(row_start, row_end + 1):
            ans.append(array[r][col_end])
        col_end -= 1
        if row_start > row_end:
            break
        for c in reversed(range(col_start, col_end + 1)):
            ans.append(array[row_end][c])
        row_end -= 1
        if col_start > col_end:
            break
        for r in reversed(range(row_start, row_end + 1)):
            ans.append(array[r][col_start])
        col_start += 1
    return ans
