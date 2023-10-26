"""
<div class="html">
<p>
  Write a function that, given a string, returns its longest palindromic
  substring.
</p>
<p>
  A palindrome is defined as a string that's written the same forward and
  backward. Note that single-character strings are palindromes.
</p>
<p>You can assume that there will only be one longest palindromic substring.</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">string</span> = "abaxyzzyxf"
</pre>
<h3>Sample Output</h3>
<pre>"xyzzyx"
</pre>
</div>
"""


def longestPalindromicSubstring(string):
    # Write your code here.
    current_longest = [0, 1]
    for i in range(1, len(string)):
        odd = get_longest_palindrome_from(string, i - 1, i + 1)
        even = get_longest_palindrome_from(string, i - 1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        current_longest = max(current_longest, longest,
                              key=lambda x: x[1] - x[0])
    return string[current_longest[0]:current_longest[1]]


def get_longest_palindrome_from(string, left_idx, right_idx):
    while left_idx >= 0 and right_idx < len(string):
        if string[left_idx] != string[right_idx]:
            break
        left_idx -= 1
        right_idx += 1
    return [left_idx + 1, right_idx]


s = "noon high it is"
print(longestPalindromicSubstring(s))
