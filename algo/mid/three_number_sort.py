def threeNumberSort(array, order):
    # Write your code here.
    rank = {number: idx for idx, number in enumerate(order)}
    k = -1
    i = 0
    j = len(array) - 1
    partition = order[1]

    while i <= j:
        if rank[array[i]] == rank[partition]:
            i += 1
        elif rank[array[i]] < rank[partition]:
            k += 1
            array[i], array[k] = array[k], array[i]
            i += 1
        else:
            array[i], array[j] = array[j], array[i]
            j -= 1

    return array


print(threeNumberSort([1,0,0,-1,-1,0,1,1], [0, 1, -1]))
