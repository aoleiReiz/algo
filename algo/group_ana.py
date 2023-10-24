
"""
<div class="html">
<p>
  Write a function that takes in an array of strings and groups anagrams together.
</p>
<p>
  Anagrams are strings made up of exactly the same letters, where order doesn't
  matter. For example, <span>"cinema"</span> and <span>"iceman"</span> are
  anagrams; similarly, <span>"foo"</span> and <span>"ofo"</span> are anagrams.
</p>
<p>
  Your function should return a list of anagram groups in no particular order.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">words</span> = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
</pre>
<h3>Sample Output</h3>
<pre>[["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
</pre>
</div>
"""

def groupAnagrams(words):
    # Write your code here.
    word_dict = {}
    for word in words:
        key = "".join(sorted([c for c in word]))
        if key not in word_dict:
            word_dict[key] = []
        word_dict[key].append(word)
    return list(word_dict.values())



w = ["zxc", "asd", "weq", "sda", "qwe", "xcz"]

print(groupAnagrams(w))