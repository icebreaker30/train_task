def dfs(leftnode,rightnode):
    if (leftnode is None and rightnode is None):
        return True
    if (leftnode is None or rightnode is None):
        return False
    if leftnode.val != rightnode.val:
        return False
    return df(leftnode.left, rightnode.right) and df(leftnode.right,rightnode.left)
return dfs(root.left, root.right)