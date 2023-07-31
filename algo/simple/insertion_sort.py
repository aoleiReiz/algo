"""
<div class="html">
<p>
  Write a function that takes in an array of integers and returns a sorted
  version of that array. Use the Insertion Sort algorithm to sort the array.
</p>
<p>
  If you're unfamiliar with Insertion Sort, we recommend watching the Conceptual
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


def insertionSort(array):
    # Write your code here.
    for i in range(len(array)):
        e = array[i]
        j = i - 1
        while j >= 0 and array[j] > e:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = e
    return array
