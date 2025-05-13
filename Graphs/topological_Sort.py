def dfs(adj, node, vis, stck):
    vis[node] = 1
    for nbr in adj[node]:
        if not vis[nbr]:
            dfs(adj, nbr, vis, stck)
    stck.append(node)


def topo(adj):
    n = len(adj)
    vis = [0] * n
    stck = []
    for i in range(n):
        if not vis[i]:
            dfs(adj, i, vis, stck)
    stck.reverse()
    return stck