"""
<div class="html">
<p>
  Write a function that takes in an array of integers representing a stack,
  recursively sorts the stack in place (i.e., doesn't create a brand new array),
  and returns it.
</p>
<p>
  The array must be treated as a stack, with the end of the array as the top of
  the stack. Therefore, you're only allowed to
</p>
<ul>
  <li>
    Pop elements from the top of the stack by removing elements from the end of
    the array using the built-in <span>.pop()</span> method in your programming
    language of choice.
  </li>
  <li>
    Push elements to the top of the stack by appending elements to the end of
    the array using the built-in <span>.append()</span> method in your
    programming language of choice.
  </li>
  <li>
    Peek at the element on top of the stack by accessing the last element in the
    array.
  </li>
</ul>
<p>
  You're not allowed to perform any other operations on the input array,
  including accessing elements (except for the last element), moving elements,
  etc.. You're also not allowed to use any other data structures, and your
  solution must be recursive.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">stack</span> = [-5, 2, -2, 4, 3, 1]
</pre>
<h3>Sample Output</h3>
<pre>[-5, -2, 1, 2, 3, 4]
</pre>
</div>
"""

def insert_in_sorted_order(stack, value):
    if len(stack) == 0 or stack[-1] <= value:
        stack.append(value)
        return
    top = stack.pop()
    insert_in_sorted_order(stack, value)
    stack.append(top)

def sortStack(stack):
    if len(stack) == 0:
        return stack

    top = stack.pop()
    sortStack(stack)
    insert_in_sorted_order(stack, top)
    return stack

