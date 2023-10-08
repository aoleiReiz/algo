"""
<div class="html">
  <p>
    You're given two Linked Lists of potentially unequal length. These Linked
    Lists potentially merge at a shared intersection node. Write a function
    that returns the intersection node or returns <span>None</span> /
    <span>null</span> if there is no intersection.
  </p>
  <p>
    Each <span>LinkedList</span> node has an integer <span>value</span> as well as
    a <span>next</span> node pointing to the next node in the list or to
    <span>None</span> / <span>null</span> if it's the tail of the list.
  </p>
  <p>
    Note: Your function should return an existing node. It should not modify
    either Linked List, and it should not create any new Linked Lists.
  </p>
  <h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">linkedListOne</span> = 2 -&gt; 3 -&gt; 1 -&gt; 4
<span class="CodeEditor-promptParameter">linkedListTwo</span> = 8 -&gt; 7 -&gt; 1 -&gt; 4
</pre>
  <h3>Sample Output</h3>
<pre>1 -&gt; 4 <span class="CodeEditor-promptComment">// The lists intersect at the node with value 1</span>
</pre>
  </div>
"""


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    visited = set()
    p1 = linkedListOne
    while p1:
        visited.add(p1)
        p1 = p1.next
    p2 = linkedListTwo
    while p2:
        if p2 in visited:
            return p2
        p2 = p2.next
    return None
