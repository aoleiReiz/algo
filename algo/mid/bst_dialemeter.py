"""
<div class="html">
<p>
  Write a function that takes in a Binary Tree and returns its diameter. The
  diameter of a binary tree is defined as the length of its longest path, even
  if that path doesn't pass through the root of the tree.
</p>
<p>
  A path is a collection of connected nodes in a tree, where no node is
  connected to more than two other nodes. The length of a path is the number of
  edges between the path's first node and its last node.
</p>
<p>
  Each <span>BinaryTree</span> node has an integer <span>value</span>, a
  <span>left</span> child node, and a <span>right</span> child node. Children
  nodes can either be <span>BinaryTree</span> nodes themselves or
  <span>None</span> / <span>null</span>.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">tree</span> =        1
            /   \
           3     2
         /   \
        7     4
       /       \
      8         5
     /           \
    9             6
</pre>
<h3>Sample Output</h3>
<pre>6 <span class="CodeEditor-promptComment">// 9 -&gt; 8 -&gt; 7 -&gt; 3 -&gt; 4 -&gt; 5 -&gt; 6</span>
<span class="CodeEditor-promptComment">// There are 6 edges between the</span>
<span class="CodeEditor-promptComment">// first node and the last node</span>
<span class="CodeEditor-promptComment">// of this tree's longest path.</span>
</pre>
</div>
"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    def helper(node: BinaryTree, height):
        if node is None:
            return height
        left_height = helper(node.left, height + 1)
        right_height = helper(node.right, height + 1)
        nonlocal max_height
        max_height = max(max_height, left_height + right_height - height * 2 - 2)
        return max(left_height, right_height)

    max_height = 0
    helper(tree, 0)
    return max_height
