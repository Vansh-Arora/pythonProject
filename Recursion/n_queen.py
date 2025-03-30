def show(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            if A[i][j] == 0:    print("- ",end='')
            else: print("Q ",end='')
        print()
    print('\n')

def isSafe(r,c,m,n):
    for i in range(r-1,-1,-1):
        if m[i][c] == 1:
            return False
    i = r-1
    j = c-1
    while i > -1 and j >-1:
        if m[i][j] ==1:
            return False
        i -=1
        j-=1
    k = r-1
    l = c+1
    while k > -1 and l < n:
        if m[k][l] == 1:
            return False
        k-=1
        l+=1

    return True
def placeNqueens(n,m,r):

    if r == n:
        show(matrix)
        return
    for c in range(n):
        if isSafe(r,c,m,n):
            m[r][c] = 1
            placeNqueens(n,m,r+1)
            m[r][c] = 0
n = 4
matrix = [[0 for _ in range(n)] for _ in range(n)]
placeNqueens(n,matrix,0)
