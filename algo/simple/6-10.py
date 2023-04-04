class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findClosestValueInBst(tree, target):
    def helper(node: BST, t, closest):
        if not node:
            return closest
        if abs(t - closest) > abs(node.value - t):
            closest = node.value
        if node.value > target:
            return helper(node.left, t, closest)
        elif node.value < target:
            return helper(node.right, t, closest)
        return closest

    return helper(tree, target, tree.value)


def branchSums(root):
    def helper(node: BinaryTree, cur_sum, ans):
        if node is None:
            return
        if node.left is None and node.right is None:
            cur_sum += node.value
            ans.append(cur_sum)
            return
        cur_sum += node.value
        if node.left is not None:
            helper(node.left, cur_sum, ans)
        if node.right is not None:
            helper(node.right, cur_sum, ans)

    ans = []
    helper(root, 0, ans)
    return ans


def nodeDepths(root):
    def helper(node, depth):
        if node is None:
            return 0
        return depth + helper(node.left, depth + 1) + helper(node.right, depth + 1)

    return helper(root, 0)
