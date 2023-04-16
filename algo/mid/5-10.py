def longestPeak(array):
    # Write your code here.
    if len(array) < 3:
        return 0
    max_count = 0
    idx = 1
    while idx < len(array) - 1:
        if array[idx - 1] < array[idx] > array[idx + 1]:
            left = idx - 1
            right = idx + 1
            while left > 0 and array[left] > array[left - 1]:
                left -= 1
            while right < len(array) - 1 and array[right] > array[right + 1]:
                right += 1
            c = right - left + 1
            if c > max_count:
                max_count = c
        idx += 1

    return max_count


def arrayOfProducts(array):
    left_dp = []
    right_dp = []
    left = right = 1
    ans = []
    for num in array:
        left_dp.append(left)
        left *= num
    for num in reversed(array):
        right_dp.append(right)
        right *= num
    for i in range(len(array)):
        ans.append(right_dp[len(array) - i - 1] * left_dp[i])
    return ans


def firstDuplicateValue(array):
    for value in array:
        value = abs(value)
        if array[value - 1] < 0:
            return value
        else:
            array[value - 1] *= -1
    return -1

if __name__ == '__main__':
    arr = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    print(longestPeak(arr))
