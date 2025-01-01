def get_time(grid):
    n = len(grid)
    m = len(grid[0])
    rotten_que = []
    fresh = 0
    for row in range(n):
        for col in range(m):
            if grid[row][col] == 2:
                rotten_que.append([(row,col),0])
            elif grid[row][col] == 1:
                fresh += 1
    time = 0
    directions = [(-1,0),(1,0),(0,-1),(0,1)] # UP DOWN LEFT RIGHT
    while rotten_que:
        curr = rotten_que.pop(0)
        cr, cc = curr[0]
        time = max(time, curr[1])
        for nr,nc in directions:
            nbr_r = cr + nr
            nbr_c = cc + nc
            if 0 <= nbr_r < n and 0 <= nbr_c <m and grid[nbr_r][nbr_c] == 1:
                fresh -= 1
                grid[nbr_r][nbr_c] = 2
                rotten_que.append([(nbr_r, nbr_c), time+1])
    if fresh > 0:
        return -1
    return time



