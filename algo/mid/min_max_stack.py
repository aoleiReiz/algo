"""
<div class="html">
<p>
  Write a <span>MinMaxStack</span> class for a Min Max Stack. The class should
  support:
</p>
<ul>
  <li>Pushing and popping values on and off the stack.</li>
  <li>Peeking at the value at the top of the stack.</li>
  <li>
    Getting both the minimum and the maximum values in the stack at any given
    point in time.
  </li>
</ul>
<p>
  All class methods, when considered independently, should run in constant time
  and with constant space.
</p>
<h3>Sample Usage</h3>
<pre><span class="CodeEditor-promptComment">// All operations below are performed sequentially.</span>
<span class="CodeEditor-promptParameter">MinMaxStack</span>(): - <span class="CodeEditor-promptComment">// instantiate a MinMaxStack</span>
<span class="CodeEditor-promptParameter">push</span>(5): -
<span class="CodeEditor-promptParameter">getMin</span>(): 5
<span class="CodeEditor-promptParameter">getMax</span>(): 5
<span class="CodeEditor-promptParameter">peek</span>(): 5
<span class="CodeEditor-promptParameter">push</span>(7): -
<span class="CodeEditor-promptParameter">getMin</span>(): 5
<span class="CodeEditor-promptParameter">getMax</span>(): 7
<span class="CodeEditor-promptParameter">peek</span>(): 7
<span class="CodeEditor-promptParameter">push</span>(2): -
<span class="CodeEditor-promptParameter">getMin</span>(): 2
<span class="CodeEditor-promptParameter">getMax</span>(): 7
<span class="CodeEditor-promptParameter">peek</span>(): 2
<span class="CodeEditor-promptParameter">pop</span>(): 2
<span class="CodeEditor-promptParameter">pop</span>(): 7
<span class="CodeEditor-promptParameter">getMin</span>(): 5
<span class="CodeEditor-promptParameter">getMax</span>(): 5
<span class="CodeEditor-promptParameter">peek</span>(): 5
</pre>
</div>
"""


class MinMaxStack:

    def __init__(self):
        self.stack = []
        self.min_max_stack = []

    def peek(self):
        # Write your code here.
        if self.stack:
            return self.stack[-1]

    def pop(self):
        # Write your code here.
        number = self.stack.pop()
        self.min_max_stack.pop()
        return number

    def push(self, number):
        # Write your code here.
        min_max = {"min": number, "max": number}
        if self.stack:
            min_max["min"] = min(self.min_max_stack[-1]["min"], min_max["min"])
            min_max["max"] = max(self.min_max_stack[-1]["max"], min_max["max"])
        self.stack.append(number)
        self.min_max_stack.append(min_max)

    def getMin(self):
        # Write your code here.
        if self.stack:
            return self.min_max_stack[-1]["min"]

    def getMax(self):
        # Write your code here.
        if self.stack:
            return self.min_max_stack[-1]["max"]
