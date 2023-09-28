"""
<div class="html">
<p>
  The pre-order traversal of a Binary Tree is a traversal technique that starts
  at the tree's root node and visits nodes in the following order:
</p>
<ol>
  <li>Current node</li>
  <li>Left subtree</li>
  <li>Right subtree</li>
</ol>
<p>
  Given a non-empty array of integers representing the pre-order traversal of a
  Binary Search Tree (BST), write a function that creates the relevant BST and
  returns its root node.
</p>
<p>
  The input array will contain the values of BST nodes in the order in which
  these nodes would be visited with a pre-order traversal.
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
<pre><span class="CodeEditor-promptParameter">preOrderTraversalValues</span> = [10, 4, 2, 1, 5, 17, 19, 18]
</pre>
<h3>Sample Output</h3>
<pre>        10
      /    \
     4      17
   /   \      \
  2     5     19
 /           /
1           18
</pre>
</div>
"""


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfoIndex:
    def __init__(self, idx):
        self.idx = idx


def reconstructBst(preOrderTraversalValues):
    def helper(tree_info_idx:TreeInfoIndex, lower_value, upper_value):
        if tree_info_idx.idx >= len(preOrderTraversalValues):
            return
        root_value = preOrderTraversalValues[tree_info_idx.idx]
        if root_value < lower_value or root_value >= upper_value:
            return None
        tree_info_idx.idx += 1
        bst = BST(root_value)
        bst.left = helper(tree_info_idx, lower_value, root_value)
        bst.right = helper(tree_info_idx, root_value, upper_value)
        return bst
    ti = TreeInfoIndex(0)
    return helper(ti, float("-inf"), float("inf"))
