"""
<div class="html">
<p>
  Given two binary trees, merge them and return the resulting tree.
  If two nodes overlap during the merger then sum the values, otherwise use the existing node.
</p>

<p>
  Note that your solution can either mutate the existing trees or return a
  new tree.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">tree1</span> =   1
        /   \
       3     2
     /   \
    7     4

<span class="CodeEditor-promptParameter">tree2</span> =   1
        /   \
       5     9
     /      / \
    2      7   6
</pre>
<h3>Sample Output</h3>
<pre><span class="CodeEditor-promptParameter">output</span> =  2
        /   \
      8      11
    /  \    /  \
  9     4  7    6
</pre>
</div>
"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def mergeBinaryTrees(tree1, tree2):
    # Write your code here.
    if tree1 is None and tree2 is None:
        return None
    elif tree1 is not None and tree2 is None:
        return tree1
    elif tree2 is not None and tree1 is None:
        return tree2
    root = BinaryTree(tree1.value + tree2.value)
    root.left = mergeBinaryTrees(tree1.left, tree2.left)
    root.right = mergeBinaryTrees(tree1.right, tree2.right)
    return root

