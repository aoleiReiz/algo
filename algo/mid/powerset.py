"""
<div class="html">
<p>
  Write a function that takes in an array of unique integers and returns its
  powerset.
</p>
<p>
  The powerset <span>P(X)</span> of a set <span>X</span> is the set of all
  subsets of <span>X</span>. For example, the powerset of <span>[1,2]</span> is
  <span>[[], [1], [2], [1,2]]</span>.
</p>
<p>
  Note that the sets in the powerset do not need to be in any particular order.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">array</span> = [1, 2, 3]
</pre>
<h3>Sample Output</h3>
<pre>[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
</pre>
</div>
"""


def powerset(array):
    def back_track(idx, cur):
        ans.append(cur[:])
        if idx >= len(array):
            return
        for i in range(idx, len(array)):
            cur.append(array[i])
            back_track(i + 1, cur)
            cur.pop()

    ans = []
    back_track(0, [])
    return ans


print(powerset([1,2,3]))
