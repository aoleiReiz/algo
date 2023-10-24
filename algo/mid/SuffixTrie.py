"""
<div class="html">
<p>
  Write a <span>SuffixTrie</span> class for a Suffix-Trie-like data structure.
  The class should have a <span>root</span> property set to be the root node of
  the trie and should support:
</p>
<ul>
  <li>
    Creating the trie from a string; this will be done by calling the
    <span>populateSuffixTrieFrom</span> method upon class instantiation, which
    should populate the <span>root</span> of the class.
  </li>
  <li>Searching for strings in the trie.</li>
</ul>
<p>
  Note that every string added to the trie should end with the special
  <span>endSymbol</span> character: <span>"*"</span>.
</p>
<p>
  If you're unfamiliar with Suffix Tries, we recommend watching the
  Conceptual Overview section of this question's video explanation before
  starting to code.
</p>
<h3>Sample Input (for creation)</h3>
<pre><span class="CodeEditor-promptParameter">string</span> = "babc"
</pre>
<h3>Sample Output (for creation)</h3>
<pre><span class="CodeEditor-promptComment">The structure below is the root of the trie.</span>
{
  "c": {"*": true},
  "b": {
    "c": {"*": true},
    "a": {"b": {"c": {"*": true}}},
  },
  "a": {"b": {"c": {"*": true}}},
}
</pre>
<h3>
  Sample Input (for searching in the suffix trie above)
</h3>
<pre><span class="CodeEditor-promptParameter">string</span> = "abc"
</pre>
<h3>
  Sample Output (for searching in the suffix trie above)
</h3>
<pre>true
</pre>
</div>
"""

class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        # Write your code here.
        for i in range(len(string)):
            self._insert_from_root(string[i:])

    def _insert_from_root(self, string):
        node = self.root
        for char in string:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.endSymbol] = True

    def contains(self, string):
        # Write your code here.
        node = self.root
        for char in string:
            if char not in node:
                return False
            node = node[char]
        return self.endSymbol in node


if __name__ == '__main__':
    sft = SuffixTrie("babc")
    print(sft.root)
    print(sft.contains("abc"))