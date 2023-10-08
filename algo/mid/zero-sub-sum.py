"""
<div class="html">
  <p>
    You're given a list of integers <span>nums</span>. Write a function that
    returns a boolean representing whether there exists a zero-sum subarray of
    <span>nums</span>.
  </p>

  <p>
    A zero-sum subarray is any subarray where all of the values add up to zero.
    A subarray is any contiguous section of the array. For the purposes of this
    problem, a subarray can be as small as one element and as long as the
    original array.
  </p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">nums</span> = [-5, -5, 2, 3, -2]</pre>
<h3>Sample Output</h3>
<pre>True <span class="CodeEditor-promptComment">// The subarray [-5, 2, 3] has a sum of 0
</span>
</pre></div>
"""

def zeroSumSubarray(nums):
    # Write your code here.
    n = len(nums)
    for i in range(n):
        cur_sum = 0
        for j in range(i, n):
            cur_sum += nums[j]
            if cur_sum == 0:
                return True
    return False

def zeroSumSubarray2(nums):
    # Write your code here.
    sums = {0}
    cur_sum = 0
    for num in nums:
        cur_sum += num
        if cur_sum in sums:
            return True
        else:
            sums.add(cur_sum)
    return False