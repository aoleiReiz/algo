"""
<div class="html">
<p>
  Write a function that takes in a Binary Tree and returns if that tree is
  symmetrical. A tree is symmetrical if the left and right subtrees are
  mirror images of each other.
</p>
<p>
  Each <span>BinaryTree</span> node has an integer <span>value</span>, a
  <span>left</span> child node, and a <span>right</span> child node. Children
  nodes can either be <span>BinaryTree</span> nodes themselves or
  <span>None</span> / <span>null</span>.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">tree</span> =    1
       /     \
      2       2
    /   \   /   \
   3     4 4     3
 /   \          /  \
5     6        6    5
</pre>
<h3>Sample Output</h3>
<pre>True</pre>
</div>
"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def symmetricalTree(tree):
    def helper(left_node: BinaryTree, right_node: BinaryTree):
        if left_node is None and right_node is None:
            return True
        elif left_node is not None and right_node is not None:
            return left_node.value == right_node.value and helper(left_node.left, right_node.right) and helper(
                left_node.right, right_node.left)
        else:
            return False
    return helper(tree, tree)