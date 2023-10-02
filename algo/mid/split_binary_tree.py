"""
<div class="jTkuHfOQH3L3HHmwPlJF  "><div class="uwUbSWm9V0ZSJ4gulz1h"><div class="ZqUsZdoA7jZWJAW3mlgZ"><span class="Hj1pF2lRQTvzyk9N2bZ_">Difficulty: </span><span class="
  k5TOGyZC96x1C44FseXE
  YTguk1dLs7iSg3asqY8h"></span></div><div class="ZqUsZdoA7jZWJAW3mlgZ"><span class="Hj1pF2lRQTvzyk9N2bZ_">Category: </span><span class="T1N9Cp_ty2K8QvDOZK0q">Hidden</span></div><div class="ZqUsZdoA7jZWJAW3mlgZ"><span class="Hj1pF2lRQTvzyk9N2bZ_">Successful Submissions: </span><span class="">1,588+</span></div></div><h2 class="wBpuKvBGWdd7o3KaUFOQ">Split Binary Tree<div class="lFcRs4PtZfHpa3dkuyaE"><div class="BfC3RTvnU7R_k49n9ahp o5z7gBjWlhcY3lFlXVEo _9YSDxfK6t2TQGYpB9UJw zID0MIsc6tojSv0ZvLZA fNNakthNj0odlRHr5YmZ"></div></div><svg viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg" class="qm8sWAa7_5ACRip3akq_"><path d="M12.821 16a.5.5 0 0 1-.203-.043L8 13.901l-4.618 2.056a.501.501 0 0 1-.694-.556L3.707 10.3.147 6.732a.502.502 0 0 1 .255-.845l5.103-1.023L7.543.272c.16-.362.753-.362.914 0l2.037 4.592 5.104 1.023a.5.5 0 0 1 .255.845l-3.56 3.567L13.31 15.4a.5.5 0 0 1-.49.6zM8 12.852c.069 0 .138.015.203.043l3.938 1.754-.882-4.417a.502.502 0 0 1 .137-.452l3.09-3.094-4.441-.89a.5.5 0 0 1-.36-.288L8 1.708l-1.686 3.8a.5.5 0 0 1-.36.288l-4.44.89 3.09 3.094c.117.118.169.288.136.452l-.882 4.417 3.939-1.754A.497.497 0 0 1 8 12.852z"></path></svg></h2><div class="TLQjVhfBX4gHWkO9qYsJ ae-workspace-light"><div class="html">
<p>
  Write a function that takes in a Binary Tree with at least one node and
  checks if that Binary Tree can be split into two Binary Trees of equal sum by
  removing a single edge. If this split is possible, return the new sum of each
  Binary Tree, otherwise return 0. Note that you do not need to return the edge
  that was removed.
</p>
<p>
  The sum of a Binary Tree is the sum of all values in that Binary Tree.
</p>
<p>
  Each <span>BinaryTree</span> node has an integer <span>value</span>, a
  <span>left</span> child node, and a <span>right</span> child node. Children
  nodes can either be <span>BinaryTree</span> nodes themselves or
  <span>None</span> / <span>null</span>.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">tree</span> =     1
        /     \
       3       -2
     /   \    /  \
    6    -5  5    2
  /
 2
</pre>
<h3>Sample Output</h3>
<pre>6 <span class="CodeEditor-promptComment">// Remove the edge to the left of the root node,
// creating two trees, each with sums of 6</span>
</pre>
</div></div><div class="ubkRh609gZAKC63eyoHt"><h3 class="vygxGX6EU5SRulNpPyt2">Hints</h3><div class="bkkMG8fczzJ203ky4pHV"><div class="
      m9qHEqW419vul78Ks_N4
      g48zh7pepCprgQNnhjYR
      mM3sM9N65X8SED6MshZA
      " tabindex="0"><div class="
      kDoyoLEgMLE4k325vN3f
      undefined
      j_lw6dN2omYx5lZJ8ABZ

      lVJy_CZchkfIT7EoMqL7"><div class="I58Rrhf2fmpCKtHv9Zj9">Hint 1</div><svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 292.362 292.362" xml:space="preserve" class="IRK2SKMnxjFj8TmtU5p0 "><path d="M286.935 69.377c-3.614-3.617-7.898-5.424-12.848-5.424H18.274c-4.952 0-9.233 1.807-12.85 5.424C1.807 72.998 0 77.279 0 82.228c0 4.948 1.807 9.229 5.424 12.847l127.907 127.907c3.621 3.617 7.902 5.428 12.85 5.428s9.233-1.811 12.847-5.428L286.935 95.074c3.613-3.617 5.427-7.898 5.427-12.847 0-4.948-1.814-9.229-5.427-12.85z"></path></svg></div><div class="wydVeRqMMtvFhbtm0Oda " style="transition: height 400ms linear 0s; height: 0px;"><div class="ya7hOTvkcvOlBTsWTi3l"><div class="U1quNvMraAr3Hbq2JfVQ"><p>
  Try first calculating the sum of the entire Binary Tree. What information does
  this give you towards solving the problem?
</p>
</div></div></div></div></div><div class="bkkMG8fczzJ203ky4pHV"><div class="
      m9qHEqW419vul78Ks_N4
      g48zh7pepCprgQNnhjYR
      mM3sM9N65X8SED6MshZA
      " tabindex="0"><div class="
      kDoyoLEgMLE4k325vN3f
      undefined
      j_lw6dN2omYx5lZJ8ABZ

      lVJy_CZchkfIT7EoMqL7"><div class="I58Rrhf2fmpCKtHv9Zj9">Hint 2</div><svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 292.362 292.362" xml:space="preserve" class="IRK2SKMnxjFj8TmtU5p0 "><path d="M286.935 69.377c-3.614-3.617-7.898-5.424-12.848-5.424H18.274c-4.952 0-9.233 1.807-12.85 5.424C1.807 72.998 0 77.279 0 82.228c0 4.948 1.807 9.229 5.424 12.847l127.907 127.907c3.621 3.617 7.902 5.428 12.85 5.428s9.233-1.811 12.847-5.428L286.935 95.074c3.613-3.617 5.427-7.898 5.427-12.847 0-4.948-1.814-9.229-5.427-12.85z"></path></svg></div><div class="wydVeRqMMtvFhbtm0Oda " style="transition: height 400ms linear 0s; height: 0px;"><div class="ya7hOTvkcvOlBTsWTi3l"><div class="U1quNvMraAr3Hbq2JfVQ">
<p>
  If the sum of the entire Binary Tree is odd, then there is no possible
  solution, because the values are all integers. Otherwise, the solution could
  be that sum divided by two, or potentially there is still no solution. What
  does the scenario look like where the solution is the sum divided by two?
</p>
</div></div></div></div></div><div class="bkkMG8fczzJ203ky4pHV"><div class="
      m9qHEqW419vul78Ks_N4
      g48zh7pepCprgQNnhjYR
      mM3sM9N65X8SED6MshZA
      " tabindex="0"><div class="
      kDoyoLEgMLE4k325vN3f
      undefined
      j_lw6dN2omYx5lZJ8ABZ

      lVJy_CZchkfIT7EoMqL7"><div class="I58Rrhf2fmpCKtHv9Zj9">Hint 3</div><svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 292.362 292.362" xml:space="preserve" class="IRK2SKMnxjFj8TmtU5p0 "><path d="M286.935 69.377c-3.614-3.617-7.898-5.424-12.848-5.424H18.274c-4.952 0-9.233 1.807-12.85 5.424C1.807 72.998 0 77.279 0 82.228c0 4.948 1.807 9.229 5.424 12.847l127.907 127.907c3.621 3.617 7.902 5.428 12.85 5.428s9.233-1.811 12.847-5.428L286.935 95.074c3.613-3.617 5.427-7.898 5.427-12.847 0-4.948-1.814-9.229-5.427-12.85z"></path></svg></div><div class="wydVeRqMMtvFhbtm0Oda " style="transition: height 400ms linear 0s; height: 0px;"><div class="ya7hOTvkcvOlBTsWTi3l"><div class="U1quNvMraAr3Hbq2JfVQ">
<p>
  There is a solution if there is a subtree that has a sum equal to the the
  total Binary Tree sum divided by two. In this case, removing the incoming
  edge to that node would have to create another Binary Tree of equal sum.
</p>
</div></div></div></div></div><div class="bkkMG8fczzJ203ky4pHV"><div class="
      m9qHEqW419vul78Ks_N4
      g48zh7pepCprgQNnhjYR
      mM3sM9N65X8SED6MshZA
      " tabindex="0"><div class="
      kDoyoLEgMLE4k325vN3f
      undefined
      j_lw6dN2omYx5lZJ8ABZ

      lVJy_CZchkfIT7EoMqL7"><div class="I58Rrhf2fmpCKtHv9Zj9">Hint 4</div><svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 292.362 292.362" xml:space="preserve" class="IRK2SKMnxjFj8TmtU5p0 "><path d="M286.935 69.377c-3.614-3.617-7.898-5.424-12.848-5.424H18.274c-4.952 0-9.233 1.807-12.85 5.424C1.807 72.998 0 77.279 0 82.228c0 4.948 1.807 9.229 5.424 12.847l127.907 127.907c3.621 3.617 7.902 5.428 12.85 5.428s9.233-1.811 12.847-5.428L286.935 95.074c3.613-3.617 5.427-7.898 5.427-12.847 0-4.948-1.814-9.229-5.427-12.85z"></path></svg></div><div class="wydVeRqMMtvFhbtm0Oda " style="transition: height 400ms linear 0s; height: 0px;"><div class="ya7hOTvkcvOlBTsWTi3l"><div class="U1quNvMraAr3Hbq2JfVQ">
<p>
  To prevent recalculating the same subtree sums, try using a post-order
  traversal of the Binary Tree. This allows you to calculate the sums of the
  smallest subtrees first, then send that information back up to the parents to
  quickly calculate their sums.
</p></div></div></div></div></div><div class="bkkMG8fczzJ203ky4pHV"><div class="
      m9qHEqW419vul78Ks_N4
      g48zh7pepCprgQNnhjYR
      mM3sM9N65X8SED6MshZA
      " tabindex="0"><div class="
      kDoyoLEgMLE4k325vN3f
      undefined
      j_lw6dN2omYx5lZJ8ABZ

      lVJy_CZchkfIT7EoMqL7"><div class="I58Rrhf2fmpCKtHv9Zj9">Optimal Space &amp; Time Complexity</div><svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 292.362 292.362" xml:space="preserve" class="IRK2SKMnxjFj8TmtU5p0 "><path d="M286.935 69.377c-3.614-3.617-7.898-5.424-12.848-5.424H18.274c-4.952 0-9.233 1.807-12.85 5.424C1.807 72.998 0 77.279 0 82.228c0 4.948 1.807 9.229 5.424 12.847l127.907 127.907c3.621 3.617 7.902 5.428 12.85 5.428s9.233-1.811 12.847-5.428L286.935 95.074c3.613-3.617 5.427-7.898 5.427-12.847 0-4.948-1.814-9.229-5.427-12.85z"></path></svg></div><div class="wydVeRqMMtvFhbtm0Oda " style="transition: height 400ms linear 0s; height: 0px;"><div class="ya7hOTvkcvOlBTsWTi3l"><div class="U1quNvMraAr3Hbq2JfVQ">O(n) time | O(h) space - where n is the number of nodes in the tree and h is the height of the tree</div></div></div></div></div></div></div>
"""

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def splitBinaryTree(tree):
    ts = get_tree_sum(tree) / 2
    can_split = try_sub_tree(tree, ts)[1]
    return ts if can_split else 0


def try_sub_tree(tree:BinaryTree, target_sum):
    if tree is None:
        return 0, False
    left_sum, left_can_split = try_sub_tree(tree.left, target_sum)
    right_sum, right_can_split = try_sub_tree(tree.right, target_sum)
    current_tree_sum = tree.value + right_sum + left_sum
    can_split = left_can_split or right_can_split or current_tree_sum == target_sum
    return current_tree_sum, can_split




def get_tree_sum(node: BinaryTree):
    if node is None:
        return 0
    left_sum = get_tree_sum(node.left)
    right_sum = get_tree_sum(node.right)
    s = left_sum + right_sum + node.value
    return s
