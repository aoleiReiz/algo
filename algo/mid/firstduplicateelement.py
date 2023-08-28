"""
<div class="html">
<p>
  Given an array of integers between <span>1</span> and <span>n</span>,
  inclusive, where <span>n</span> is the length of the array, write a function
  that returns the first integer that appears more than once (when the array is
  read from left to right).
</p>
<p>
  In other words, out of all the integers that might occur more than once in the
  input array, your function should return the one whose first duplicate value
  has the minimum index.
</p>
<p>
  If no integer appears more than once, your function should return
  <span>-1</span>.
</p>
<p>Note that you're allowed to mutate the input array.</p>
<h3>Sample Input #1</h3>
<pre><span class="CodeEditor-promptParameter">array</span> = [2, 1, 5, 2, 3, 3, 4]
</pre>
<h3>Sample Output #1</h3>
<pre>2 <span class="CodeEditor-promptComment">// 2 is the first integer that appears more than once.</span>
<span class="CodeEditor-promptComment">// 3 also appears more than once, but the second 3 appears after the second 2.</span>
</pre>
<h3>Sample Input #2</h3>
<pre><span class="CodeEditor-promptParameter">array</span> = [2, 1, 5, 3, 3, 2, 4]
</pre>
<h3>Sample Output #2</h3>
<pre>3 <span class="CodeEditor-promptComment">// 3 is the first integer that appears more than once.</span>
<span class="CodeEditor-promptComment">// 2 also appears more than once, but the second 2 appears after the second 3.</span>
</pre>
</div>
"""

def firstDuplicateValue(array):
    for num in array:
        value = abs(array[num - 1])
        if array[value - 1] < 0:
            return value
        else:
            array[value - 1] *= -1
    return array
