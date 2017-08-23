# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def findTarget(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: bool
    """
    num_hash = {}
    return find(root, k, num_hash)


def find(root, k, num_hash):
    if root == None:
        return False
    if (k - root.val) in num_hash:
        return True
    num_hash[root.val] = 1
    return find(root.left, k, num_hash) or find(root.right, k, num_hash)


# [5,3,6,2,4,None,7]
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)


target = 30
print(findTarget(root, target))