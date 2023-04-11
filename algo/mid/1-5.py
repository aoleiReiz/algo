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

