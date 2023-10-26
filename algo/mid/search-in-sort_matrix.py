"""
<div class="html">
<p>
  You're given a two-dimensional array (a matrix) of distinct integers and a
  target integer. Each row in the matrix is sorted, and each column is also sorted; the
  matrix doesn't necessarily have the same height and width.
</p>
<p>
  Write a function that returns an array of the row and column indices of the
  target integer if it's contained in the matrix, otherwise
  <span>[-1, -1]</span>.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">matrix</span> = [
  [1, 4, 7, 12, 15, 1000],
  [2, 5, 19, 31, 32, 1001],
  [3, 8, 24, 33, 35, 1002],
  [40, 41, 42, 44, 45, 1003],
  [99, 100, 103, 106, 128, 1004],
]
<span class="CodeEditor-promptParameter">target</span> = 44
</pre>
<h3>Sample Output</h3>
<pre>[3, 3]
</pre>
</div>
"""


def searchInSortedMatrix(matrix, target):
    # Write your code here.
    r = len(matrix) - 1

    c = 0
    while r >= 0 and c < len(matrix[0]):
        if matrix[r][c] == target:
            return [r, c]
        elif matrix[r][c] > target:
            r -= 1
        else:
            c += 1
    return [-1,-1]

