"""
<div class="html">
<p>
  Write a function that takes in an array of at least three integers and,
  without sorting the input array, returns a sorted array of the three largest
  integers in the input array.
</p>
<p>
  The function should return duplicate integers if necessary; for example, it
  should return <span>[10, 10, 12]</span> for an input array of
  <span>[10, 5, 9, 10, 12]</span>.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">array</span> = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
</pre>
<h3>Sample Output</h3>
<pre>[18, 141, 541]
</pre>
</div>
"""
def findThreeLargestNumbers(array):
    # Write your code here.
    first = float("-inf")
    second = float("-inf")
    third = float("-inf")
    for num in array:
        if num > first:
            first, second, third = num, first, second
        elif num > second:
            second, third = num, second
        elif num > third:
            third = num
    return [third, second, first]

