class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        stack = [root,root]
        while stack:
            r1 = stack.pop()
            r2 = stack.pop()
            if r1 == None and r2 == None:
                continue
            if r1 == None or r2 == None:
                return False
            if r1.val != r2.val:
                return False
            stack.append(r1.left)
            stack.append(r2.right)
            stack.append(r1.right)
            stack.append(r2.left)
        return True
