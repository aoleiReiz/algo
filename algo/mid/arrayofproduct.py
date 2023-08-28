"""
<div class="html">
<p>
  Write a function that takes in a non-empty array of integers and returns an
  array of the same length, where each element in the output array is equal to
  the product of every other number in the input array.
</p>
<p>
  In other words, the value at <span>output[i]</span> is equal to the product of
  every number in the input array other than <span>input[i]</span>.
</p>
<p>Note that you're expected to solve this problem without using division.</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">array</span> = [5, 1, 4, 2]
</pre>
<h3>Sample Output</h3>
<pre>[8, 40, 10, 20]
<span class="CodeEditor-promptComment">// 8 is equal to 1 x 4 x 2</span>
<span class="CodeEditor-promptComment">// 40 is equal to 5 x 4 x 2</span>
<span class="CodeEditor-promptComment">// 10 is equal to 5 x 1 x 2</span>
<span class="CodeEditor-promptComment">// 20 is equal to 5 x 1 x 4</span>
</pre>
</div>
"""


def arrayOfProducts(array):
    ans = []
    left_dp = [1] * len(array)
    right_dp = [1] * len(array)
    for i, num in enumerate(array):
        if i > 0:
            left_dp[i] = left_dp[i - 1] * array[i - 1]
    for i in reversed(range(len(array))):
        if i < len(array) - 1:
            right_dp[i] = right_dp[i + 1] * array[i + 1]
    for i in range(len(array)):
        ans.append(left_dp[i] * right_dp[i])

    return ans


arr = [5, 1, 4, 2]
print(arrayOfProducts(arr))
