"""
<div class="html">
<p>
  You're given the head of a Singly Linked List whose nodes are in sorted order
  with respect to their values. Write a function that returns a modified version
  of the Linked List that doesn't contain any nodes with duplicate values. The
  Linked List should be modified in place (i.e., you shouldn't create a brand
  new list), and the modified Linked List should still have its nodes sorted
  with respect to their values.
</p>
<p>
  Each <span>LinkedList</span> node has an integer <span>value</span> as well as
  a <span>next</span> node pointing to the next node in the list or to
  <span>None</span> / <span>null</span> if it's the tail of the list.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">linkedList</span> = 1 -&gt; 1 -&gt; 3 -&gt; 4 -&gt; 4 -&gt; 4 -&gt; 5 -&gt; 6 -&gt; 6 <span class="CodeEditor-promptComment">// the head node with value 1</span>
</pre>
<h3>Sample Output</h3>
<pre>1 -&gt; 3 -&gt; 4 -&gt; 5 -&gt; 6 <span class="CodeEditor-promptComment">// the head node with value 1</span>
</pre>
</div>
"""

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    p = linkedList
    while p and p.next:
        if p.value == p.next.value:
            p.next = p.next.next
        else:
            p = p.next

    return linkedList
