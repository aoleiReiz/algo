"""
<div class="html">
<p>
  Write a function that takes in a non-empty sorted array of distinct integers,
  constructs a BST from the integers, and returns the root of the BST.
</p>
<p>
  The function should minimize the height of the BST.
</p>
<p>
  You've been provided with a <span>BST</span> class that you'll have to use to
  construct the BST.
</p>
<p>
  Each <span>BST</span> node has an integer <span>value</span>, a
  <span>left</span> child node, and a <span>right</span> child node. A node is
  said to be a valid <span>BST</span> node if and only if it satisfies the BST
  property: its <span>value</span> is strictly greater than the values of every
  node to its left; its <span>value</span> is less than or equal to the values
  of every node to its right; and its children nodes are either valid
  <span>BST</span> nodes themselves or <span>None</span> / <span>null</span>.
</p>
<p>
  A BST is valid if and only if all of its nodes are valid
  <span>BST</span> nodes.
</p>
<p>
  Note that the <span>BST</span> class already has an <span>insert</span> method
  which you can use if you want.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">array</span> = [1, 2, 5, 7, 10, 13, 14, 15, 22]
</pre>
<h3>Sample Output</h3>
<pre>         10
       /     \
      2      14
    /   \   /   \
   1     5 13   15
          \       \
           7      22
<span class="CodeEditor-promptComment">// This is one example of a BST with min height</span>
<span class="CodeEditor-promptComment">// that you could create from the input array.</span>
<span class="CodeEditor-promptComment">// You could create other BSTs with min height</span>
<span class="CodeEditor-promptComment">// from the same array; for example:</span>
         10
       /     \
      5      15
    /   \   /   \
   2     7 13   22
 /           \
1            14
</pre>
</div>
"""


def minHeightBst(array):
    def helper(arr, left, right):
        if left > right:
            return
        mid = (left + right) // 2
        node = BST(arr[mid])
        node.left = helper(arr, left, mid - 1)
        node.right = helper(arr, mid + 1, right)
        return node

    return helper(array, 0, len(array) - 1)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

    def __str__(self):
        return str(self.value)


def in_order_traverse(node:BST):
    if node:
        in_order_traverse(node.left)
        print(node.value)
        in_order_traverse(node.right)


if __name__ == '__main__':
    a = [1, 2, 5, 7, 10, 13, 14, 15, 22]
    root = minHeightBst(a)
    in_order_traverse(root)
