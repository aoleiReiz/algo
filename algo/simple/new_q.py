# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    s = 0
    if tree is not None:
        if tree.value > 0:
            return tree.value
        elif tree.value == -1:
            s = s + (evaluateExpressionTree(tree.left) + evaluateExpressionTree(tree.right))
        elif tree.value == -2:
            s = s + (evaluateExpressionTree(tree.left) - evaluateExpressionTree(tree.right))
        elif tree.value == -3:
            s = s + (evaluateExpressionTree(tree.left) // evaluateExpressionTree(tree.right))
        else:
            s = s + (evaluateExpressionTree(tree.left) * evaluateExpressionTree(tree.right))
    return s


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    fast = linkedList
    slow = linkedList
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow
