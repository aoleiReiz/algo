"""<div class="html">
<p>
  Write a function that takes in two non-empty arrays of integers, finds the
  pair of numbers (one from each array) whose absolute difference is closest to
  zero, and returns an array containing these two numbers, with the number from
  the first array in the first position.
</p>
<p>
  Note that the absolute difference of two integers is the distance between
  them on the real number line. For example, the absolute difference of -5 and 5
  is 10, and the absolute difference of -5 and -4 is 1.
</p>
<p>
  You can assume that there will only be one pair of numbers with the smallest
  difference.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">arrayOne</span> = [-1, 5, 10, 20, 28, 3]
<span class="CodeEditor-promptParameter">arrayTwo</span> = [26, 134, 135, 15, 17]
</pre>
<h3>Sample Output</h3>
<pre>[28, 26]</pre>
</div>"""

def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne = sorted(arrayOne)
    arrayTwo = sorted(arrayTwo)
    idx1 = 0
    idx2 = 0
    smallest_difference = float("inf")
    smallest_difference_pair = []
    while idx1 < len(arrayOne) and idx2 < len(arrayTwo):
        diff = abs(arrayOne[idx1] - arrayTwo[idx2])
        if diff < smallest_difference:
            smallest_difference = diff
            smallest_difference_pair = [arrayOne[idx1] , arrayTwo[idx2]]
        if arrayOne[idx1] > arrayTwo[idx2]:
            idx2 += 1
        elif arrayOne[idx1] < arrayTwo[idx2]:
            idx1 += 1
        else:
            return smallest_difference_pair
    return smallest_difference_pair

