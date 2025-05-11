from collections import deque
def bfs(root, adj_list):
    if root == None:
        return
    visited = [0 for i in range(len(adj_list))]
    que = deque([root])
    visited[root] = 1
    ans = []

    while que:
        curr_trav = []
        length = len(que)
        for _ in range(length):
            curr = que.popleft()
            curr_trav.append(curr)
            for each in adj_list[curr]:
                if not visited[each]:
                    visited[each] = 1
                    que.append(each)

        ans.append(curr_trav)

    return ans




adj_list = [[],
[2, 3],
[1, 4, 5],
[1, 4],
[3, 2, 5],
[2, 4]]

print(bfs(1, adj_list))