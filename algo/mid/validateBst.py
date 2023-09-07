"""
<div class="html">
<p>
  Write a function that takes in a potentially invalid Binary Search Tree (BST)
  and returns a boolean representing whether the BST is valid.
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
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">tree</span> =   10
       /     \
      5      15
    /   \   /   \
   2     5 13   22
 /           \
1            14
</pre>
<h3>Sample Output</h3>
<pre>true</pre>
</div>
"""

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    def helper(node, min_node, max_node):
        if node is None:
            return True
        if min_node is not None and min_node.value > node.value:
            return False
        if max_node is not None and max_node.value <= node.value:
            return False
        return helper(node.left, min_node, node) and helper(node.right, node, max_node)
    return helper(tree, None, None)
