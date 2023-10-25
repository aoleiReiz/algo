"""
<div class="html">
<p>
  Write a function that takes in an array of integers and returns a new array
  containing, at each index, the next element in the input array that's greater
  than the element at that index in the input array.
</p>
<p>
  In other words, your function should return a new array where
  <span>outputArray[i]</span> is the next element in the input array that's
  greater than <span>inputArray[i]</span>. If there's no such next greater
  element for a particular index, the value at that index in the output array
  should be <span>-1</span>. For example, given <span>array = [1, 2]</span>,
  your function should return <span>[2, -1]</span>.
</p>
<p>
  Additionally, your function should treat the input array as a
  <b>circular</b> array. A circular array wraps around itself as if it were
  connected end-to-end. So the next index after the last index in a circular
  array is the first index. This means that, for our problem, given
  <span>array = [0, 0, 5, 0, 0, 3, 0, 0]</span>, the next greater element after
  <span>3</span> is <span>5</span>, since the array is circular.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">array</span> = [2, 5, -3, -4, 6, 7, 2]
</pre>
<h3>Sample Output</h3>
<pre>[5, 6, 6, 6, 7, -1, 5]
</pre>
</div>
"""

def nextGreaterElement(array):
    # Write your code here.
    stack = []
    n = len(array)
    ans = [-1] * n
    for idx in range(2 * n):
        cur_idx = idx % n

        while stack and array[stack[-1]] < array[cur_idx]:
            top = stack.pop()
            ans[top] = array[cur_idx]

        stack.append(cur_idx)
    return ans