# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    def helper(node: BST, min_node: BST, max_node: BST):
        if node is None:
            return True
        if min_node and node.value < min_node.value:
            return False
        if max_node and node.value >= max_node.value:
            return False
        return helper(node.left, min_node, node) and helper(node.right, node, max_node)

    return helper(tree, None, None)


def inOrderTraverse(tree, array):
    def helper(tree):
        if tree:
            helper(tree.left)
            array.append(tree.value)
            helper(tree.right)

    helper(tree)
    return array


def preOrderTraverse(tree, array):
    def helper(tree):
        if tree:
            array.append(tree.value)
            helper(tree.left)
            helper(tree.right)

    helper(tree)
    return array


def postOrderTraverse(tree, array):
    def helper(tree):
        if tree:
            helper(tree.left)
            helper(tree.right)
            array.append(tree.value)

    helper(tree)
    return array
