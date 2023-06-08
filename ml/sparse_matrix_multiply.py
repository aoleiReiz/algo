def sparse_matrix_multiplication(matrix_a, matrix_b):
    # Write your code here.
    am = len(matrix_a)
    bm = len(matrix_b)
    if am == 0 or bm == 0 or len(matrix_a[0]) == 0 or len(matrix_b[0]) == 0:
        return [[]]
    an = len(matrix_a[0])
    bn = len(matrix_b[0])
    if an != bm:
        return [[]]
    matrix_c = [[0 for _ in range(bn)] for _ in range(am)]
    for i in range(am):
        for j in range(bn):
            s = 0
            for k in range(an):
                s += matrix_a[i][k] * matrix_b[k][j]
            matrix_c[i][j] = s
    return matrix_c


def sparse_matrix_multiplication2(matrix_a, matrix_b):
    # Write your code here.
    am = len(matrix_a)
    bm = len(matrix_b)
    if am == 0 or bm == 0 or len(matrix_a[0]) == 0 or len(matrix_b[0]) == 0:
        return [[]]
    an = len(matrix_a[0])
    bn = len(matrix_b[0])
    if an != bm:
        return [[]]
    matrix_c = [[0 for _ in range(bn)] for _ in range(am)]
    sparse_a = get_dict_of_nonzero_cells(matrix_a)
    sparse_b = get_dict_of_nonzero_cells(matrix_b)
    for i, k in sparse_a.keys():
        for j in range(len(matrix_b[0])):
            if (k, j) in sparse_b.keys():
                matrix_c[i][j] = sparse_a[(i, k)] * sparse_b[(k, j)]
    return matrix_c


def get_dict_of_nonzero_cells(matrix):
    dict_of_nonzero_cells = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                dict_of_nonzero_cells[(i, j)] = matrix[i][j]
    return dict_of_nonzero_cells
