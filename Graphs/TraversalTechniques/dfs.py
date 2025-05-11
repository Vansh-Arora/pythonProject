def helper(root, adj_list, visited, traversal):
    if root == None:
        return
    if not visited[root]:
        visited[root] = 1
        traversal.append(root)
        for each in adj_list[root]:
            helper(each,adj_list,visited,traversal)


def dfs(root, adj_list):
    ans = []
    visited = [0 for _ in range(len(adj_list))]
    helper(root, adj_list, visited, ans)
    return ans


adj_list = [[],
[2, 3],
[1, 4, 5],
[1, 4],
[3, 2, 5],
[2, 4]]
print(dfs(1, adj_list))

