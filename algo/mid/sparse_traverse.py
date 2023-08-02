"""
<div class="html">
<p>
  Write a function that takes in an n x m two-dimensional array (that can be
  square-shaped when n == m) and returns a one-dimensional array of all the
  array's elements in spiral order.
</p>
<p>
  Spiral order starts at the top left corner of the two-dimensional array, goes
  to the right, and proceeds in a spiral pattern all the way until every element
  has been visited.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">array</span> = [
  [1,   2,  3, 4],
  [12, 13, 14, 5],
  [11, 16, 15, 6],
  [10,  9,  8, 7],
]
</pre>
<h3>Sample Output</h3>
<pre>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
</pre>
</div>
"""


def spiralTraverse(array):
    # Write your code here.
    n_row = len(array)
    ans = []
    if n_row == 0:
        return ans

    n_col = len(array[0])
    row_start = 0
    col_start = 0
    col_end = n_col - 1
    row_end = n_row - 1

    while row_start <= row_end and col_start <= col_end:
        # 左上 -> 右上
        for c in range(col_start, col_end + 1):
            ans.append(array[row_start][c])
        row_start += 1

        if row_start > row_end:
            break
        # 右上 -> 右下
        for r in range(row_start, row_end + 1):
            ans.append(array[r][col_end])
        col_end -= 1

        # 右下 -> 左下
        for c in reversed(range(col_start, col_end + 1)):
            ans.append(array[row_end][c])
        row_end -= 1


        if col_start > col_end:
            break

        for r in reversed(range(row_start, row_end + 1)):
            ans.append(array[r][col_start])
        col_start += 1

    return ans


print(spiralTraverse( [
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]
  ]))