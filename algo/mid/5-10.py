def longestPeak(array):
    # Write your code here.
    if len(array) < 3:
        return 0
    max_count = 0
    idx = 1
    while idx < len(array) - 1:
        if array[idx - 1] < array[idx] > array[idx + 1]:
            left = idx - 1
            right = idx + 1
            while left > 0 and array[left] > array[left - 1]:
                left -= 1
            while right < len(array) - 1 and array[right] > array[right + 1]:
                right += 1
            c = right - left + 1
            if c > max_count:
                max_count = c
        idx += 1

    return max_count


def arrayOfProducts(array):
    left_dp = []
    right_dp = []
    left = right = 1
    ans = []
    for num in array:
        left_dp.append(left)
        left *= num
    for num in reversed(array):
        right_dp.append(right)
        right *= num
    for i in range(len(array)):
        ans.append(right_dp[len(array) - i - 1] * left_dp[i])
    return ans


def firstDuplicateValue(array):
    for value in array:
        value = abs(value)
        if array[value - 1] < 0:
            return value
        else:
            array[value - 1] *= -1
    return -1


def mergeOverlappingIntervals(intervals):
    # Write your code here.
    if len(intervals) == 0:
        return [[]]
    intervals = sorted(intervals, key=lambda x: x[0])
    ans = []
    prev_interval = intervals[0]
    for interval in intervals[1:]:
        if interval[0] > prev_interval[1]:
            ans.append(prev_interval)
            prev_interval = interval
        else:
            prev_interval[1] = max(interval[1], prev_interval[1])
    ans.append(prev_interval)
    return ans


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

    def contains(self, value):
        # Write your code here.
        if self.value == value:
            return True
        elif self.value > value:
            return self.left.contains(value)
        else:
            return self.right.catains(value)

    def remove(self, value, parent=None):
        # Write your code here.
        # Do not edit the return statement of this method.
        if value < self.value:
            if self.left is not None:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right is not None:
                self.right.remove(value, self)
        if self.left is not None and self.right is not None:
            self.value = self.right.getMinValue()
            self.right.remove(self.value, self)
        elif parent is None:
            if self.left is not None:
                self.value = self.left.value
                self.right = self.left.right
                self.left = self.left.left
            elif self.right is not None:
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
            else:
                pass
        elif parent.left == self:
            parent.left = self.left if self.left is not None else self.right
        elif parent.right == self:
            parent.right = self.left if self.left is not None else self.right
        return self

    def getMinValue(self):
        if self.left is None:
            return self.value
        else:
            return self.left.getMinValue()


if __name__ == '__main__':
    arr = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    print(longestPeak(arr))
