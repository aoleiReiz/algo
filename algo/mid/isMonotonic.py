"""<div class="html">
<p>
  Write a function that takes in an array of integers and returns a boolean
  representing whether the array is monotonic.
</p>
<p>
  An array is said to be monotonic if its elements, from left to right, are
  entirely non-increasing or entirely non-decreasing.
</p>
<p>
  Non-increasing elements aren't necessarily exclusively decreasing; they simply
  don't increase. Similarly, non-decreasing elements aren't necessarily
  exclusively increasing; they simply don't decrease.
</p>
<p>Note that empty arrays and arrays of one element are monotonic.</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">array</span> = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
</pre>
<h3>Sample Output</h3>
<pre>true
</pre>
</div>"""

def isMonotonic(array):
    # Write your code here.
    if len(array) <= 2:
        return True
    flag = 0 if array[0] == array[-1] else (1 if array[0] > array[-1] else -1)

    for idx in range(1, len(array)):
        if flag == 0:
            if array[idx - 1] != array[idx]:
                return False
        elif flag == 1:
            if array[idx - 1] < array[idx]:
                return False
        else:
            if array[idx - 1] > array[idx]:
                return False

    return True