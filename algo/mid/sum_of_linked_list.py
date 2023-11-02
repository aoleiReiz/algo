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
# This is an input class. Do not edit.


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    p_head = LinkedList(-1)
    p = p_head
    p1, p2 = linkedListOne, linkedListTwo
    exceed_digit = 0
    value = 0
    while p1 or p2:
        value = exceed_digit
        if p1:
            value += p1.value
            p1 = p1.next
        if p2:
            value += p2.value
            p2 = p2.next
        exceed_digit = value // 10
        value = value % 10
        p.next = LinkedList(value)
        p = p.next
    if exceed_digit > 1:
        p.next = LinkedList(exceed_digit)
    return p_head.next


l11 = LinkedList(2)
l12 = LinkedList(4)
l13 = LinkedList(7)
l14 = LinkedList(1)
l11.next = l12
l12.next = l13
l13.next = l14

l21 = LinkedList(9)
l22 = LinkedList(4)
l23 = LinkedList(5)
l21.next = l22
l22.next = l23

p = sumOfLinkedLists(l11, l21)
while p:
    print(p.value, end="=>")
    p = p.next
print("None")
