"""
<div class="html">
<p>
  Write a function that takes in an array of integers and returns a sorted
  version of that array. Use the Bubble Sort algorithm to sort the array.
</p>
<p>
  If you're unfamiliar with Bubble Sort, we recommend watching the Conceptual
  Overview section of this question's video explanation before starting to code.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">array</span> = [8, 5, 2, 9, 5, 6, 3]
</pre>
<h3>Sample Output</h3>
<pre>[2, 3, 5, 5, 6, 8, 9]
</pre>
</div>
"""

def bubbleSort(array):
    # Write your code here.
    for _ in range(len(array)):
        changed_flag = False
        for j in reversed(range(1, len(array))):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                changed_flag = True
        if not changed_flag:
            break
    return array