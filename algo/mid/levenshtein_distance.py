"""
<div class="html">
<p>
  Write a function that takes in two strings and returns the minimum number of
  edit operations that need to be performed on the first string to obtain the
  second string.
</p>
<p>
  There are three edit operations: insertion of a character, deletion of a
  character, and substitution of a character for another.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">str1</span> = "abc"
<span class="CodeEditor-promptParameter">str2</span> = "yabd"
</pre>
<h3>Sample Output</h3>
<pre>2 <span class="CodeEditor-promptComment">// insert "y"; substitute "c" for "d"</span>
</pre>
</div>
"""

def levenshteinDistance(str1, str2):
    m = len(str1)
    n = len(str2)

    dp = [[0 for _ in range(n+1)] for _ in range(m + 1)]
    for i in range(n+1):
        dp[0][i] = i
    for i in range(m + 1):
        dp[i][0] = i

    for i in range(1, m + 1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1)

    return dp[m][n]