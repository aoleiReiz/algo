"""
<div class="html">
<p>
  You're given two positive integers representing the height of a staircase and
  the maximum number of steps that you can advance up the staircase at a time.
  Write a function that returns the number of ways in which you can climb the
  staircase.
</p>
<p>
  For example, if you were given a staircase of <span>height = 3</span> and
  <span>maxSteps = 2</span> you could climb the staircase in 3 ways. You could
  take <b>1 step, 1 step, then 1 step</b>, you could also take
  <b>1 step, then 2 steps</b>, and you could take <b>2 steps, then 1 step</b>.
</p>
<p>Note that <span>maxSteps &lt;= height</span> will always be true.</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">height</span> = 4
<span class="CodeEditor-promptParameter">maxSteps</span> = 2
</pre>
<h3>Sample Output</h3>
<pre>5
<span class="CodeEditor-promptComment">// You can climb the staircase in the following ways: </span>
<span class="CodeEditor-promptComment">// 1, 1, 1, 1</span>
<span class="CodeEditor-promptComment">// 1, 1, 2</span>
<span class="CodeEditor-promptComment">// 1, 2, 1</span>
<span class="CodeEditor-promptComment">// 2, 1, 1</span>
<span class="CodeEditor-promptComment">// 2, 2</span>
</pre>
</div>
"""


def staircaseTraversal(height, maxSteps):
    # Write your code here.
    def helper(h):
        if h in memo:
            return memo[h]
        s = 0
        for idx in range(1, min(maxSteps, h) + 1):
            s += helper(h - idx)
        memo[h] = s
        return s

    memo = {}

    return helper(height)
