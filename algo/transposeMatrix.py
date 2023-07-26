"""
<div class="html">
  <p>
    You're given a 2D array of integers <span>matrix</span>. Write a function
    that returns the transpose of the matrix.
  </p>

  <p>
    The transpose of a matrix is a flipped version of the original matrix across
    its main diagonal (which runs from top-left to bottom-right); it switches
    the row and column indices of the original matrix.
  </p>

  <p>
    You can assume the input matrix always has at least 1 value; however its
    width and height are not necessarily the same.
  </p>

  <h3>Sample Input #1</h3>
  <pre><span class="CodeEditor-promptParameter">matrix</span> = [
  [1, 2],
]</pre>
  <h3>Sample Output # 1</h3>
  <pre>[
  [1],
  [2]
]</pre>

  <h3>Sample Input #2</h3>
  <pre><span class="CodeEditor-promptParameter">matrix</span> = [
  [1, 2],
  [3, 4],
  [5, 6]
]</pre>
  <h3>Sample Output #2</h3>
  <pre>[
  [1, 3, 5],
  [2, 4, 6]
]</pre>

  <h3>Sample Input #3</h3>
  <pre><span class="CodeEditor-promptParameter">matrix</span> = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]</pre>
  <h3>Sample Output #3</h3>
  <pre>[
  [1, 4, 7],
  [2, 5, 8],
  [3, 6, 9]
]</pre>
</div>
"""
def transposeMatrix(matrix):
    # Write your code here.
    n_rows = len(matrix)
    if n_rows == 0:
        return []
    n_cols = len(matrix[0])
    ans = [[0 for _ in range(n_rows)]for _ in range(n_cols)]
    for i in range(n_cols):
        for j in range(n_rows):
            ans[i][j] = matrix[j][i]
    return ans