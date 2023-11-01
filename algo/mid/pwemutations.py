"""
<div class="html">
<p>
  Write a function that takes in an array of unique integers and returns an
  array of all permutations of those integers in no particular order.
</p>
<p>If the input array is empty, the function should return an empty array.</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">array</span> = [1, 2, 3]
</pre>
<h3>Sample Output</h3>
<pre>[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
</pre>
</div>
"""


def getPermutations(array):
    # Write your code here.
    def back_track(cur: list, visited: list):
        if len(cur) == len(array) and cur:
            ans.append(cur[:])
        for idx in range(len(array)):
            if not visited[idx]:
                cur.append(array[idx])
                visited[idx] = True
                back_track(cur, visited)
                cur.pop()
                visited[idx] = False

    ans = []
    back_track([], [False] * len(array))
    return ans

print(getPermutations([1,2,3]))