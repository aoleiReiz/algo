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
            ans.append([array[idx], * r])
    return ans