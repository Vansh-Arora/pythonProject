def create_undirected_graph_matrix():
    n, m = map(int, input().split())
    graph = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(m):
        n1, n2 = map(int, input().split())
        graph[n1][n2] = 1
        graph[n2][n1] = 1

    for row in graph:
        print(row)

def create_undirected_graph_list():
    n, m = map(int, input().split())
    adj_list = [[] for j in range(n+1)]
    for i in range(m):
        n1, n2 = map(int, input().split())
        adj_list[n1].append(n2)
        adj_list[n2].append(n1)

    for row in adj_list:
        print(row)




create_undirected_graph_list()
create_undirected_graph_matrix()