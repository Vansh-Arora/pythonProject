from typing import final


def is_safe(maze, visited, i, j, n):
    if i in range(0,n) and j in range(0,n) and maze[i][j] and not visited[i][j]:
        return True
    return False

def solve(maze, visited, i, j, n, ans, final_ans):
    if i == n-1 and j == n-1:
        final_ans.append(ans[:])
        return

    visited[i][j] = 1

    #UP
    if is_safe(maze, visited, i-1, j, n):
        ans.append('U')
        solve(maze, visited, i-1, j, n, ans, final_ans)
        ans.pop()

    #Down
    if is_safe(maze, visited, i+1, j, n):
        ans.append('D')
        solve(maze, visited, i+1, j, n, ans, final_ans)
        ans.pop()

    #Left
    if is_safe(maze, visited, i, j-1, n):
        ans.append('L')
        solve(maze, visited, i, j-1, n, ans, final_ans)
        ans.pop()

    #Right
    if is_safe(maze, visited, i, j+1, n):
        ans.append('R')
        solve(maze, visited, i, j+1, n, ans, final_ans)
        ans.pop()
    visited[i][j] = 0

if __name__ == "__main__":
    n = 4
    visited_arr = [[0 for _ in range(n)] for _ in range(n)]
    maze = [
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1],
        [0, 0, 1, 1]
    ]
    final_ans = []
    solve(maze, visited_arr, 0, 0, n, [], final_ans)
    print(final_ans)