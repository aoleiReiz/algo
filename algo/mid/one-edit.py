"""
<div class="html">
  <p>
    You're given two strings <span>stringOne</span> and <span>stringTwo</span>.
    Write a function that determines if these two strings can be made equal
    using only one edit.
  </p>

  <p>
    There are 3 possible edits:
    </p><ul>
      <li>
        <b>Replace</b>: One character in one string is swapped for a different
        character.
      </li>
      <li>
        <b>Add</b>: One character is added at any index in one string.
      </li>
      <li>
        <b>Remove</b>: One character is removed at any index in one string.
      </li>
    </ul>
  <p></p>

  <p>
    Note that both strings will contain at least one character. If the strings
    are the same, your function should return true.
  </p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">stringOne</span> = "hello"
<span class="CodeEditor-promptParameter">stringTwo</span> = "hollo"
</pre>
<h3>Sample Output</h3>
<pre>True <span class="CodeEditor-promptComment">// A single replace at index 1 of either string can make the strings equal</span>
</pre>
</div>
"""

def oneEdit(stringOne, stringTwo):
    len_one = len(stringOne)
    len_two = len(stringTwo)
    if abs(len_one - len_two) > 1:
        return False

    made_edit = False
    idx_one = 0
    idx_two = 0

    while idx_one < len_one and idx_two < len_two:
        if stringOne[idx_one] != stringTwo[idx_two]:
            if made_edit:
                return False
            made_edit = True

            if len_one > len_two:
                idx_one += 1
            elif len_two > len_one:
                idx_two += 1
            else:
                idx_one += 1
                idx_two += 1
        else:
            idx_one += 1
            idx_two += 1

    return True