def dfs_cycle(adj, node, vis):
    vis[node] = 2
    for nbr in adj[node]:
        if not vis[nbr]:
            if dfs_cycle(adj, nbr, vis):
                return True
        elif vis[nbr] == 2:
            return True
    vis[node] = 1
    return False


def is_cyclic(adj):
    n = len(adj)
    vis = [0] * n
    for i in range(n):
        if not vis[i]:
            if dfs_cycle(adj, i, vis):
                return True
    return False