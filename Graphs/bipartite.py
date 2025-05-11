## LEETCODE TEMPLATE: https://leetcode.com/problems/is-graph-bipartite/submissions/1631046440/
## DFS Approach
class Solution:
    def isBipartite(self, graph) -> bool:
        vis = [-1 for _ in range(len(graph))]

        def dfs(start):
            for nbr in graph[start]:
                if vis[nbr] == -1:
                    vis[nbr] = 1 - vis[start]
                    if not dfs(nbr):
                        return False
                elif vis[nbr] == vis[start]:
                    return False
            return True

        for i in range(len(vis)):
            if vis[i] == -1:
                vis[i] = 1
                if not dfs(i):
                    return False
        return True

## BFS APPROACH
class Solution:
    def isBipartite(self, graph) -> bool:
        vis = [-1 for _ in range(len(graph))]
        for i in range(len(vis)):
            if vis[i] == -1:
                que = [i]
                vis[i] = 1
                while que:
                    curr = que.pop(0)
                    for nbr in graph[curr]:
                        if vis[nbr] == -1:
                            vis[nbr] = 1 - vis[curr]
                            que.append(nbr)
                        elif vis[nbr] == vis[curr]:
                            return False
        return True



