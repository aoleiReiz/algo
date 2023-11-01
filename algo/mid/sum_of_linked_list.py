"""
<div class="html">
<p>
  You're given two Linked Lists of potentially unequal length. Each Linked List
  represents a non-negative integer, where each node in the Linked List is a
  digit of that integer, and the first node in each Linked List always
  represents the least significant digit of the integer. Write a function that
  returns the head of a new Linked List that represents the sum of the integers
  represented by the two input Linked Lists.
</p>
<p>
  Each <span>LinkedList</span> node has an integer <span>value</span> as well as
  a <span>next</span> node pointing to the next node in the list or to
  <span>None</span> / <span>null</span> if it's the tail of the list. The
  <span>value</span> of each <span>LinkedList</span> node is always in the range
  of <span>0 - 9</span>.
</p>
<p>
  Note: your function must create and return a new Linked List, and you're not
  allowed to modify either of the input Linked Lists.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">linkedListOne</span> = 2 -&gt; 4 -&gt; 7 -&gt; 1
<span class="CodeEditor-promptParameter">linkedListTwo</span> = 9 -&gt; 4 -&gt; 5
</pre>
<h3>Sample Output</h3>
<pre>1 -&gt; 9 -&gt; 2 -&gt; 2
<span class="CodeEditor-promptComment">// linkedListOne represents 1742</span>
<span class="CodeEditor-promptComment">// linkedListTwo represents 549</span>
<span class="CodeEditor-promptComment">// 1742 + 549 = 2291</span>
</pre>
</div>
"""
