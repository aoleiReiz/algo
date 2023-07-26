def sweetAndSavory(dishes, target):
    dishes = sorted(dishes)
    if len(dishes) < 2:
        return [0, 0]
    if dishes[0] >= 0 or dishes[-1] <= 0:
        return [0, 0]

    best_diff = float("inf")
    best_pair = []
    left = 0
    right = len(dishes) - 1
    while left < right:
        curr_pair_sum = dishes[left] + dishes[right]
        valid = True
        if 0 < target < curr_pair_sum:
            valid = False
        if dishes[left] >= 0 or dishes[right] <= 0:
            valid = False

        if valid and curr_pair_sum == target:
            return [dishes[left], dishes[right]]
        else:
            diff = abs(curr_pair_sum - target)
            if valid and diff < best_diff:
                best_pair = [dishes[left], dishes[right]]
                best_diff = diff
            if curr_pair_sum > target:
                right -= 1
            else:
                left += 1
    return best_pair
