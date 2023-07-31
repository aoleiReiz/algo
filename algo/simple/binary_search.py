"""
<div class="html">
<p>
  Write a function that takes in a sorted array of integers as well as a target
  integer. The function should use the Binary Search algorithm to determine if
  the target integer is contained in the array and should return its index if it
  is, otherwise <span>-1</span>.
</p>
<p>
  If you're unfamiliar with Binary Search, we recommend watching the Conceptual
  Overview section of this question's video explanation before starting to code.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">array</span> = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
<span class="CodeEditor-promptParameter">target</span> = 33
</pre>
<h3>Sample Output</h3>
<pre>3
</pre>
</div>
"""
def binarySearch(array, target):
    # Write your code here.
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

