"""
<div class="html">
<p>
  Given a non-empty string of lowercase letters and a non-negative integer
  representing a key, write a function that returns a new string obtained by
  shifting every letter in the input string by k positions in the alphabet,
  where k is the key.
</p>
<p>
  Note that letters should "wrap" around the alphabet; in other words, the
  letter <span>z</span> shifted by one returns the letter <span>a</span>.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">string</span> = "xyz"
<span class="CodeEditor-promptParameter">key</span> = 2
</pre>
<h3>Sample Output</h3>
<pre>"zab"
</pre>
</div>
"""

def caesarCipherEncryptor(string, key):
    # Write your code here.
    characters = "abcdefghijklmnopqrstuvwxyz"
    char_2_idx = {char: idx for idx, char in enumerate(characters)}
    key %= 26
    new_chars = []
    for char in string:
        new_char = characters[(char_2_idx[char] + key) % 26]
        new_chars.append(new_char)
    return "".join(new_chars)