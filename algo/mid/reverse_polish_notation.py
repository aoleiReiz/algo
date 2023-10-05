"""
<div class="html">
  <p>
    You're given a list of string <span>tokens</span> representing a mathematical
    expression using Reverse Polish Notation. Reverse Polish Notation is a
    notation where operators come after operands, instead of between them. For
    example <span>2 4 +</span> would evaluate to <span>6</span>.
  </p>

  <p>
    Parenthesis are always implicit in Reverse Polish Notation, meaning an
    expression is evaluated from left to right. All of the operators for this
    problem take two operands, which will always be the two values immediately
    preceding the operator. For example, <span>18 4 - 7 /</span> would
    evaluate to <span>((18 - 4) / 7)</span> or <span>2</span>.
  </p>

  <p>
    Write a function that takes this list of <span>tokens</span> and returns
    the result. Your function should support four operators: <span>+</span>,
    <span>-</span>, <span>*</span>, and <span>/</span> for addition,
    subtraction, multiplication, and division respectively.
  </p>

  <p>
    Division should always be treated as integer division, rounding towards
    zero. For example, <span>3 / 2</span> evaluates to <span>1</span> and
    <span>-3 / 2</span> evaluates to <span>-1</span>. You can assume the
    input will always be valid Reverse Polish Notation, and it will always
    result in a valid number. Your code should not edit this input list.
  </p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">tokens</span> = ["50", "3", "17", "+", "2", "-", "/"]
</pre>
<h3>Sample Output</h3>
<pre>2 <span class="CodeEditor-promptComment">// (50 / ((3 + 17) - 2)))</span>
</pre>
</div>
"""

def reversePolishNotation(tokens):
    # Write your code here.
    stack = []
    for token in tokens:
        if token[-1].isdigit():
            stack.append(token)
        else:
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            if token == "+":
                r = num1 + num2
            elif token == '-':
                r = num1 - num2
            elif token == '*':
                r = num1 * num2
            else:
                r = num1 / num2
            stack.append(r)
    return stack[0]


if __name__ == '__main__':
    a = ["10", "-5", "*"]
    print(reversePolishNotation(a))