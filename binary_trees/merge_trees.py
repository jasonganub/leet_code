class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            t1.val = t1.val + t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1
        elif t1:
            t1.left = self.mergeTrees(t1.left, None)
            t1.right = self.mergeTrees(t1.right, None)
            return t1
        elif t2:
            t2.left = self.mergeTrees(t2.left, None)
            t2.right = self.mergeTrees(t2.right, None)
            return t2
        else:
            return None


if __name__ == '__main__':
    s = Solution()

    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.right = TreeNode(2)
    t1.left.left = TreeNode(5)

    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.right = TreeNode(3)
    t2.left.right = TreeNode(4)
    t2.right.right = TreeNode(7)



    s.mergeTrees(t1, t2)


