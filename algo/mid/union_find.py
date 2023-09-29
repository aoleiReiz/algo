# Do not edit the class below except for
# the constructor and the createSet, find,
# and union methods. Feel free to add new
# properties and methods to the class.
class UnionFind:
    def __init__(self):
        # Write your code here
        self.data = {}
        self.rank = {}

    def createSet(self, value):
        # Write your code here
        self.data[value] = value
        self.rank[value] = 1

    def find(self, value):
        # Write your code here
        if value not in self.data:
            return
        while value in self.data and self.data[value] != value:
            self.data[value] = self.data[self.data[value]]
            value = self.data[value]
        return value

    def union(self, valueOne, valueTwo):
        # Write your code here
        root_one = self.find(valueOne)
        root_two = self.find(valueTwo)
        if root_one is None or root_two is None:
            return
        if root_one != root_two:
            if self.rank[root_one] < self.rank[root_two]:
                self.data[root_one] = root_two
                self.rank[root_two] = max(self.rank[root_one] + 1, self.rank[root_two])
            else:
                self.data[root_two] = root_one
                self.rank[root_one] = max(self.rank[root_two] + 1, self.rank[root_one])