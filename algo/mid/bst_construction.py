# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
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
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif self.value == value:
            return True
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)

    def remove(self, value, parent=None):
        # Write your code here.
        # Do not edit the return statement of this method.
        if value < self.value:
            if self.left is not None:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right is not None:
                self.right.remove(value, self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.min_value()
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
            else:
                if parent.left == self:
                    parent.left = self.left if self.left is not None else self.right
                elif parent.right == self:
                    parent.right = self.right if self.right is not None else self.left

        return self

    def min_value(self):
        if self.left is not None:
            return self.left.min_value()

        return self.value
