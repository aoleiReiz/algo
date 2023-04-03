def twoNumberSum(array, targetSum):
    array = sorted(array)
    l = 0
    r = len(array) - 1
    while l < r:
        s = array[l] + array[r]
        if s > targetSum:
            r -= 1
        elif s < targetSum:
            l += 1
        else:
            return [array[l], array[r]]
    return []


def isValidSubsequence(array, sequence):
    arr_idx = 0
    seq_idx = 0
    while arr_idx < len(array) and seq_idx < len(sequence):
        if array[arr_idx] == sequence[seq_idx]:
            seq_idx += 1
        arr_idx += 1
    return seq_idx == len(sequence)


def sortedSquaredArray(array):
    array = [ number ** 2 for number in array]
    l = 0
    r = len(array) - 1
    ans = []
    while l <= r:
        if array[l] <= array[r]:
            ans.append(array[r])
            r -= 1
        else:
            ans.append(array[l])
            l += 1
    return ans[::-1]
