"""
<div class="html">
<p>
  Write a function that takes in an array of integers and returns the length of
  the longest peak in the array.
</p>
<p>
  A peak is defined as adjacent integers in the array that are <b>strictly</b>
  increasing until they reach a tip (the highest value in the peak), at which
  point they become <b>strictly</b> decreasing. At least three integers are required to
  form a peak.
</p>
<p>
  For example, the integers <span>1, 4, 10, 2</span> form a peak, but the
  integers <span>4, 0, 10</span> don't and neither do the integers
  <span>1, 2, 2, 0</span>. Similarly, the integers <span>1, 2, 3</span> don't
  form a peak because there aren't any strictly decreasing integers after the
  <span>3</span>.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">array</span> = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
</pre>
<h3>Sample Output</h3>
<pre>6 <span class="CodeEditor-promptComment">// 0, 10, 6, 5, -1, -3</span>
</pre>
</div>
"""


def longestPeak(array):
    # Write your code here.
    longest_peak = 0
    for idx in range(1, len(array) - 1):
        if array[idx - 1] < array[idx] > array[idx + 1]:
            # left
            left = idx - 1
            while left >= 0 and array[left] < array[left + 1]:
                left -= 1
            right = idx + 1
            while right < len(array) and array[right] < array[right - 1]:
                right += 1

            if right - left - 1 > longest_peak:
                longest_peak = right - left - 1
    return longest_peak


arr = [1, 3 , 2]
print(longestPeak(arr))