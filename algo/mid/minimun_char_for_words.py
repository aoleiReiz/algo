"""
<div class="html">
<p>
  Write a function that takes in an array of words and returns the smallest
  array of characters needed to form all of the words. The characters don't need
  to be in any particular order.
</p>
<p>
  For example, the characters <span>["y", "r", "o", "u"]</span> are needed to
  form the words <span>["your", "you", "or", "yo"]</span>.
</p>
<p>
  Note: the input words won't contain any spaces; however, they might contain
  punctuation and/or special characters.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">words</span> = ["this", "that", "did", "deed", "them!", "a"]
</pre>
<h3>Sample Output</h3>
<pre>["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]
<span class="CodeEditor-promptComment">// The characters could be ordered differently.</span>
</pre>
</div>
"""

def minimumCharactersForWords(words):
    # Write your code here.
    d = {}
    for word in words:
        cur = {}
        for c in word:
            cur[c] = cur.get(c,0) + 1
        for key, value in cur.items():
            d[key] = max(d.get(key, 0), value)
    ans = []
    for key, value in d.items():
        while value > 0:
            ans.append(key)
            value -= 1
    return ans