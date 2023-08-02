"""
<div class="html">
<p>
  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. The function should find all triplets in
  the array that sum up to the target sum and return a two-dimensional array of
  all these triplets. The numbers in each triplet should be ordered in ascending
  order, and the triplets themselves should be ordered in ascending order with
  respect to the numbers they hold.
</p>
<p>
  If no three numbers sum up to the target sum, the function should return an
  empty array.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">array</span> = [12, 3, 1, 2, -6, 5, -8, 6]
<span class="CodeEditor-promptParameter">targetSum</span> = 0
</pre>
<h3>Sample Output</h3>
<pre>[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
</pre>
</div>
"""
def threeNumberSum(array, targetSum):
    # Write your code here.
    def two_sum(arr, target):
        left = 0
        right = len(arr) - 1
        ans = []
        while left < right:
            s = arr[left] + arr[right]
            if s == target:
                ans.append([arr[left], arr[right]])
                left += 1
                right -= 1
            elif s > target:
                right -= 1
            else:
                left += 1
        return ans

    triplets = []
    for i in range(len(array) - 2):
        target = targetSum - array[i]
        ret = two_sum(array[i+1:], target)
        if ret:
            for r in ret:
                triplets.append([array[i], * r])
    return triplets



