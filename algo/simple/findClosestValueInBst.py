"""
<div class="html">
<p>
  Write a function that takes in a Binary Search Tree (BST) and a target integer
  value and returns the closest value to that target value contained in the BST.
</p>
<p>You can assume that there will only be one closest value.</p>
<p>
  Each <span>BST</span> node has an integer <span>value</span>, a
  <span>left</span> child node, and a <span>right</span> child node. A node is
  said to be a valid <span>BST</span> node if and only if it satisfies the BST
  property: its <span>value</span> is strictly greater than the values of every
  node to its left; its <span>value</span> is less than or equal to the values
  of every node to its right; and its children nodes are either valid
  <span>BST</span> nodes themselves or <span>None</span> / <span>null</span>.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">tree</span> =   10
       /     \
      5      15
    /   \   /   \
   2     5 13   22
 /           \
1            14
<span class="CodeEditor-promptParameter">target</span> = 12
</pre>
<h3>Sample Output</h3>
<pre>13</pre>
</div>
"""

def findClosestValueInBst(tree, target):
    def helper(node: BST, target, closest_value):
        if node is None:
            return closest_value
        if abs(target - node.value) < abs(node.value - target):
            closest_value = node.value
        if target > node.value:
            return helper(node.right, target, closest_value)
        elif target < node.value:
            return helper(node.left, target, closest_value)
        else:
            return closest_value
    return helper(tree, target, tree.value)


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
