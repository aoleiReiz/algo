""""
<div class="html">
<p>
  Write a function that takes a positive integer represented as a string
  <span>number</span> and an integer <span>numDigits</span>.
  Remove <span>numDigits</span> from the string so that the number represented
  by the string is as large as possible afterwards.
</p>
<p>
  Note that the order of the remaining digits cannot be changed. You can assume
  <span>numDigits</span> will always be less than the length of <span>number</span>
  and greater than or equal to 0.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">number</span> = "462839"
<span class="CodeEditor-promptParameter">numDigits</span> = 2
</pre>
<h3>Sample Output</h3>
<pre>"6839" <span class="CodeEditor-promptComment">// remove digits 4 and 2</span>
</pre>
</div>
"""


def bestDigits(number, numDigits):
    # Write your code here.
    stack = []
    for digit in number:
        while numDigits > 0 and len(stack) > 0 and digit > stack[-1]:
            numDigits -= 1
            stack.pop()
        stack.append(digit)
    while numDigits > 0:
        numDigits -= 1
        stack.pop()

    return "".join(stack)


if __name__ == '__main__':
    print(bestDigits("321", 1))
