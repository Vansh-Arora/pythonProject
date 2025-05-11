def lca(root, n1, n2):
    if not root or root.val == n1.val or root.val == n2.val:
        return root
    left =lca(root.left,n1,n2)
    right = lca(root.right,n1,n2)

    if left and right:
        return root
    return left if left else right
