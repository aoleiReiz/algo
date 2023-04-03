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
    array = [number ** 2 for number in array]
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


def tournamentWinner(competitions, results):
    score_dict = {}
    final_winner = ""
    max_score = -1
    for i, competition in enumerate(competitions):
        winner = competition[0] if results[i] == 1 else competition[1]
        if winner not in score_dict:
            score_dict[winner] = 3
        else:
            score_dict[winner] += 3
        if score_dict[winner] > max_score:
            max_score = score_dict[winner]
            final_winner = winner
    return final_winner


def nonConstructibleChange(coins):
    # Write your code here.
    coins = sorted(coins)
    res = 0
    for i, coin in enumerate(coins):
        if coin - res > 1:
            return res + 1
        res += coin
    return res + 1
