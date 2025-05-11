def getPath(root,key,ans):
    if not root:
        return False
    
    if root.val == key:
        return True

    ans.append(root.val)
    if (getPath(root.left,key,ans) or getPath(root.right,key,ans)):
        return True
    ans.pop()

    return False
