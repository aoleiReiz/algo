"""
<div class="html">
  <p>
    You're given an unordered list of unique integers <span>nums</span> in the
    range <span>[1, n]</span>, where <span>n</span> represents the length of
    <span>nums + 2</span>. This means that two numbers in this range are missing
    from the list.
  </p>

  <p>
    Write a func_tion that takes in this list and returns a new list with the two
    missing numbers, sorted numerically.
  </p>

  <h3>Sample Input</h3>
  <pre><span class="CodeEditor-promptParameter">nums</span> = [1, 4, 3]</pre>
  <h3>Sample Output</h3>
  <pre>[2, 5] <span class="CodeEditor-promptComment"> // n is 5, meaning the completed list should be [1, 2, 3, 4, 5]</span>
</pre>
</div>
"""


def missingNumbers(nums):
    # Write your code here.
    n = len(nums) + 2
    s = set(nums)
    r = []
    for i in range(1, n + 1):
        if i not in s:
            r.append(i)
    return r


def missingNumbers2(nums):
    n = len(nums) + 2
    total_sum = n * (n + 1) / 2
    current_sum = sum(nums)
    target_sum = (total_sum - current_sum) // 2
    first_half_sum = sum([i for i in range(1, n + 1) if i <= target_sum])
    current_first_half_sum = sum([i for i in nums if i <= target_sum])
    second_half_sum = sum([i for i in range(1, n + 1) if i > target_sum])
    current_second_half_sum = sum([i for i in nums if i > target_sum])
    return [first_half_sum - current_first_half_sum, second_half_sum - current_second_half_sum]



if __name__ == '__main__':
    ns = [1,3,4,5]
    print(missingNumbers2(ns))