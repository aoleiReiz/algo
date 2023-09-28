"""
<div class="html">
<p>
  Write a function that takes in a Binary Search Tree (BST) and a positive
  integer <span>k</span> and returns the kth largest integer contained in the
  BST.
</p>
<p>
  You can assume that there will only be integer values in the BST and that
  <span>k</span> is less than or equal to the number of nodes in the tree.
</p>
<p>
  Also, for the purpose of this question, duplicate integers will be treated as
  distinct values. In other words, the second largest value in a BST containing
  values <span>{5, 7, 7}</span> will be <span>7</span>—not <span>5</span>.
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
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">tree</span> =   15
       /     \
      5      20
    /   \   /   \
   2     5 17   22
 /   \
1     3
<span class="CodeEditor-promptParameter">k</span> = 3
</pre>
<h3>Sample Output</h3>
<pre>17</pre>
</div>
"""

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, value, num_of_visited):
        self.value = value
        self.num_of_visited = num_of_visited


def reverse_traverse(tree_info:TreeInfo, node:BST, k:int):
    if node is None:
        return
    reverse_traverse(tree_info, node.right, k)
    if tree_info.num_of_visited < k:
        tree_info.value = node.value
        tree_info.num_of_visited += 1
        reverse_traverse(tree_info, node.left, k)




def findKthLargestValueInBst(tree, k):
    tree_info = TreeInfo(0, -1)
    reverse_traverse(tree_info, tree, k)
    return tree_info.value