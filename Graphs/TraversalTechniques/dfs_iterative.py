def dfs_iterative(node, adj_list):
    n = len(adj_list)
    visited = [0]*n
    stck = [node]
    res = []
    while stck:
        curr = stck.pop()
        if not visited[curr]:
            visited[curr] = 1
            res.append(curr)
            stck.extend(adj_list[curr])
    return res

adj_list = [[],
[2, 3],
[1, 4, 5],
[1, 4],
[3, 2, 5],
[2, 4]]
print(dfs_iterative(1, adj_list))
