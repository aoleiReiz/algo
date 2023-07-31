"""
<div class="html">
<p>
  Write a function that takes in a non-empty string and that returns a boolean
  representing whether the string is a palindrome.
</p>
<p>
  A palindrome is defined as a string that's written the same forward and
  backward. Note that single-character strings are palindromes.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">string</span> = "abcdcba"
</pre>
<h3>Sample Output</h3>
<pre>true <span class="CodeEditor-promptComment">// it's written the same forward and backward</span>
</pre>
</div>
"""
def isPalindrome(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True
