class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root.val == p.val or root.val == q.val:
            return root
        queue = collections.deque([root])
        parent = {}
        while not (p in parent and q in parent):
            u = queue.popleft()
            if u.left:
                parent[u.left] = u
                queue.append(u.left)
            if u.right:
                parent[u.right] = u
                queue.append(u.right)

        res = set()
        trav = p
        while trav in parent:
            res.add(trav)
            trav = parent[trav]
        res.add(root)
        trav = q
        while not trav in res:
            trav = parent[trav]
        return trav
