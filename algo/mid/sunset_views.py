"""
<div class="html">
<p>
  Given an array of buildings and a direction that all of the buildings face,
  return an array of the indices of the buildings that can see the sunset.
</p>
<p>
  A building can see the sunset if it's strictly taller than all of the
  buildings that come after it in the direction that it faces.
</p>
<p>
  The input array named <span>buildings</span> contains positive, non-zero
  integers representing the heights of the buildings. A building at index
  <span>i</span> thus has a height denoted by <span>buildings[i]</span>. All of
  the buildings face the same direction, and this direction is either east or
  west, denoted by the input string named <span>direction</span>, which will
  always be equal to either <span>"EAST"</span> or <span>"WEST"</span>. In
  relation to the input array, you can interpret these directions as right for
  east and left for west.
</p>
<p>
  Important note: the indices in the ouput array should be sorted in ascending
  order.
</p>
<h3>Sample Input #1</h3>
<pre><span class="CodeEditor-promptParameter">buildings</span> = [3, 5, 4, 4, 3, 1, 3, 2]
<span class="CodeEditor-promptParameter">direction</span> = "EAST"
</pre>
<h3>Sample Output #1</h3>
<pre>[1, 3, 6, 7]

<span class="CodeEditor-promptComment">// Below is a visual representation of the sample input.</span>
<span class="CodeEditor-promptComment">//    _</span>
<span class="CodeEditor-promptComment">//   | |_ _</span>
<span class="CodeEditor-promptComment">//  _| | | |_   _</span>
<span class="CodeEditor-promptComment">// | | | | | | | |_</span>
<span class="CodeEditor-promptComment">// | | | | | |_| | |</span>
<span class="CodeEditor-promptComment">// |_|_|_|_|_|_|_|_|</span>
</pre>
<h3>Sample Input #2</h3>
<pre><span class="CodeEditor-promptParameter">buildings</span> = [3, 5, 4, 4, 3, 1, 3, 2]
<span class="CodeEditor-promptParameter">direction</span> = "WEST"
</pre>
<h3>Sample Output #2</h3>
<pre>[0, 1]

<span class="CodeEditor-promptComment">// The buildings are the same as in the first sample</span>
<span class="CodeEditor-promptComment">// input, but their direction is reversed.</span>
</pre>
</div>
"""

def sunsetViews(buildings, direction):
    # Write your code here.
    ans = []
    cur_max = -1
    n = len(buildings)
    iter_range = range(n)
    if direction == "EAST":
        iter_range = reversed(iter_range)
    for idx in iter_range:
        if buildings[idx] > cur_max:
            ans.append(idx)
            cur_max = buildings[idx]
    if direction == "EAST":
        ans = ans[::-1]
    return ans





    return ans
